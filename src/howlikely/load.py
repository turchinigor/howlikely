from pathlib import Path

import polars as pl
import polars.selectors as cs

ROOT = Path(__file__).parents[2]
ROAD_PATH = ROOT / "data/raw/ihme_gbd2023_road/IHME-GBD_2023_DATA-road_accidents.csv"


def load_road_data(path=ROAD_PATH):
    return (
        pl.read_csv(path)
        # IDs and columns that hold a single value everywhere
        .drop(cs.ends_with("_id"), "measure_name", "population_group_name")
        .rename(
            {
                "location_name": "country",
                "sex_name": "sex",
                "age_name": "age",
                "cause_name": "cause",
            }
        )
        # one row per country/sex/age/cause/year; Number and Rate become columns
        .pivot(
            on="metric_name",
            index=["country", "sex", "age", "cause", "year"],
            values=["val", "upper", "lower"],
        )
        .rename(
            {
                "val_Number": "deaths",
                "lower_Number": "deaths_lower",
                "upper_Number": "deaths_upper",
                "val_Rate": "rate",
                "lower_Rate": "rate_lower",
                "upper_Rate": "rate_upper",
            }
        )
    )
