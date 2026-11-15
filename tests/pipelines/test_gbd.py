from pathlib import Path

import pytest
from conftest import TABLE, TABLE_95

from howlikely_etl.gbd import combine_exports


def test_combines_both_layouts(raw_dir: Path) -> None:
    df = combine_exports(raw_dir)

    assert df.height == 3  # the twice-downloaded 95+ file counts once
    assert set(df["sex"]) == {"Male", "Female"}
    assert set(df["location_id"]) == {61}
    assert set(df["cause_id"]) == {689}
    female = df.filter(sex="Female", age_group="20-24 years").row(0, named=True)
    assert female["rate_per_100k"] == pytest.approx(4.10)
    assert female["precision"] == "2dp"
    old = df.filter(sex="Female", age_group="95+ years").row(0, named=True)
    assert old["rate_per_100k"] == pytest.approx(1152.37)  # thousands separator parsed


def test_all_causes_gets_gbd_id(raw_dir: Path) -> None:
    (raw_dir / "gbd_results_all_causes.csv").write_text(
        TABLE.replace("Road injuries", "All causes"), encoding="utf-8"
    )
    df = combine_exports(raw_dir)
    assert df.filter(cause_name="All causes")["cause_id"].to_list() == [294]


def test_conflicting_duplicates_rejected(raw_dir: Path) -> None:
    (raw_dir / "gbd_results_95+_females_v2.csv").write_text(
        TABLE_95.replace("1,152.37", "1,152.99"), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="Conflicting"):
        combine_exports(raw_dir)


def test_unknown_location_rejected(raw_dir: Path) -> None:
    (raw_dir / "gbd_results_x.csv").write_text(
        TABLE.replace("Republic of Moldova", "Atlantis"), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="no ID"):
        combine_exports(raw_dir)


def test_requires_full_download(tmp_path: Path) -> None:
    (tmp_path / "gbd_results_20-24_females.csv").write_text(TABLE, encoding="utf-8")
    with pytest.raises(FileNotFoundError):
        combine_exports(tmp_path)
