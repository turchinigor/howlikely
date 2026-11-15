from pathlib import Path

import pytest

FULL = """\
population_group_id,population_group_name,measure_id,measure_name,location_id,location_name,sex_id,sex_name,age_id,age_name,cause_id,cause_name,metric_id,metric_name,year,val,upper,lower
1,All Population,1,Deaths,61,Republic of Moldova,1,Male,9,20-24 years,689,Road injuries,3,Rate,2023,17.904075,24.492219,13.110201
"""  # noqa: E501

TABLE_HEADER = (
    "\ufeffPopulation Group,Measure,Metric,Cause,Location,Age,Sex,Year,Value,Upper,Lower\n"
)
TABLE = TABLE_HEADER + (
    "All Population,Deaths,Rate,Road injuries,Republic of Moldova,20-24 years,Females,2023,"
    "4.10,5.20,3.00\n"
)
TABLE_95 = TABLE_HEADER + (
    "All Population,Deaths,Rate,Road injuries,Republic of Moldova,95+ years,Females,2023,"
    '"1,152.37","1,300.00","1,000.10"\n'
)


@pytest.fixture
def raw_dir(tmp_path: Path) -> Path:
    """One full download plus table exports, including one file downloaded twice."""
    (tmp_path / "IHME-GBD_2023_DATA-test.csv").write_text(FULL, encoding="utf-8")
    (tmp_path / "gbd_results_20-24_females.csv").write_text(TABLE, encoding="utf-8")
    (tmp_path / "gbd_results_95+_females.csv").write_text(TABLE_95, encoding="utf-8")
    (tmp_path / "gbd_results_95+__females.csv").write_text(TABLE_95, encoding="utf-8")
    return tmp_path
