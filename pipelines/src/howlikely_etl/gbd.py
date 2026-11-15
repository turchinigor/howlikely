"""Combine GBD Results tool CSV exports into one tidy table of death rates.

The GBD Results tool produces two CSV layouts:

- full download (``IHME-GBD_*.csv``): snake_case columns with IDs, full-precision values.
- table export (``gbd_results_*.csv``): display headers, names only, values rounded to
  2 decimals, sex as "Males"/"Females".

Table-export rows get their location and cause IDs from the full downloads, so at least one
full download covering every location and cause must be present.
"""

from pathlib import Path

import polars as pl

KEY = ["location_id", "sex", "age_group", "cause_id", "year"]

COLUMNS = [
    "location_id",
    "location_name",
    "sex",
    "age_group",
    "cause_id",
    "cause_name",
    "year",
    "rate_per_100k",
    "lower",
    "upper",
    "precision",
    "source_file",
]

TABLE_EXPORT_RENAMES = {
    "Location": "location_name",
    "Sex": "sex",
    "Age": "age_group",
    "Cause": "cause_name",
    "Year": "year",
    "Value": "rate_per_100k",
    "Upper": "upper",
    "Lower": "lower",
}

# GBD cause IDs for causes that may only arrive in table exports (no full download carries them).
KNOWN_CAUSES = pl.DataFrame({"cause_id": [294], "cause_name": ["All causes"]})

SEX_NAMES = {"Male": "Male", "Males": "Male", "Female": "Female", "Females": "Female"}


def _check_scope(df: pl.DataFrame, path: Path, measure: str, metric: str) -> None:
    """Reject files that are not 'All Population' death rates."""
    for column, expected in ((measure, "Deaths"), (metric, "Rate")):
        found = set(df[column].unique().to_list())
        if found != {expected}:
            raise ValueError(f"{path.name}: expected {column} {expected!r}, found {sorted(found)}")


def _read_full(path: Path) -> pl.DataFrame:
    df = pl.read_csv(path)
    _check_scope(df, path, "measure_name", "metric_name")
    return df.select(
        "location_id",
        "location_name",
        pl.col("sex_name").alias("sex"),
        pl.col("age_name").alias("age_group"),
        "cause_id",
        "cause_name",
        "year",
        pl.col("val").alias("rate_per_100k"),
        "lower",
        "upper",
        pl.lit("full").alias("precision"),
        pl.lit(path.name).alias("source_file"),
    )


def _read_table_export(path: Path, ids: pl.DataFrame) -> pl.DataFrame:
    # Values use thousands separators ("1,152.37"), so read them as text first.
    df = pl.read_csv(path, infer_schema=False)
    df = df.rename({c: c.lstrip("\ufeff") for c in df.columns})
    _check_scope(df, path, "Measure", "Metric")
    df = df.rename(TABLE_EXPORT_RENAMES).with_columns(
        pl.col("rate_per_100k", "lower", "upper").str.replace_all(",", "").cast(pl.Float64),
        pl.col("year").cast(pl.Int64),
        pl.lit("2dp").alias("precision"),
        pl.lit(path.name).alias("source_file"),
    )
    locations = ids.select("location_id", "location_name").unique()
    causes = pl.concat([ids.select("cause_id", "cause_name"), KNOWN_CAUSES]).unique()
    df = df.join(locations, on="location_name", how="left").join(
        causes, on="cause_name", how="left"
    )
    unmatched = df.filter(pl.col("location_id").is_null() | pl.col("cause_id").is_null())
    if unmatched.height:
        names = unmatched.select("location_name", "cause_name").unique().head(5).rows()
        raise ValueError(f"{path.name}: no ID for location/cause names, e.g. {names}")
    return df.select(COLUMNS)


def combine_exports(raw_dir: Path) -> pl.DataFrame:
    """Read every GBD export in ``raw_dir`` and return one deduplicated, validated table."""
    full_files = sorted(raw_dir.glob("IHME-GBD_*.csv"))
    table_files = sorted(raw_dir.glob("gbd_results*.csv"))
    if not full_files:
        raise FileNotFoundError(f"No full GBD download (IHME-GBD_*.csv) in {raw_dir}")

    full = pl.concat([_read_full(p) for p in full_files])
    frames = [full, *(_read_table_export(p, full) for p in table_files)]
    df = pl.concat([f.select(COLUMNS) for f in frames], how="vertical_relaxed")
    df = df.with_columns(pl.col("sex").replace_strict(SEX_NAMES))

    # The same rows can arrive twice (e.g. a file downloaded twice). Identical values are
    # dropped; differing values for one key are an error.
    values = ["rate_per_100k", "lower", "upper"]
    df = df.unique(subset=[*KEY, *values], keep="first", maintain_order=True)
    conflicts = df.filter(pl.struct(KEY).is_duplicated())
    if conflicts.height:
        raise ValueError(f"Conflicting values for {conflicts.height} rows, e.g. {conflicts.row(0)}")

    # Some causes (e.g. conflict) have lower == value == upper up to float noise (~1e-15).
    tol = 1e-9
    bad_bounds = df.filter(
        (pl.col("lower") > pl.col("rate_per_100k") + tol)
        | (pl.col("rate_per_100k") > pl.col("upper") + tol)
    )
    if bad_bounds.height:
        raise ValueError(f"{bad_bounds.height} rows fall outside their uncertainty interval")

    return df.sort(["sex", "age_group", "location_name", "cause_name"])
