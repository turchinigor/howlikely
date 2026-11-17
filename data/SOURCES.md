# Data sources

`data/raw/` and `data/processed/` are git-ignored. Download the files below and put them in the
folders shown. Never edit a raw file: fix things in code and write the result to `data/processed/`.

## `raw/ihme_gbd2023_road/` (main source)

- **File:** `IHME-GBD_2023_DATA-road_accidents.csv`
- **From:** IHME GBD Results tool, https://vizhub.healthdata.org/gbd-results/
- **Downloaded:** 2026-11-17
- **Query:** Deaths; Number + Rate; 204 countries; 2023; Both / Male / Female;
  All ages + Age-standardized; causes: Transport injuries, Road injuries, Pedestrian, Cyclist,
  Motorcyclist, Motor vehicle, Other road, Other transport injuries
- **License:** IHME free-of-charge non-commercial user agreement. TODO: confirm public display
  and redistribution terms.
- **Cite:** Global Burden of Disease Collaborative Network. Global Burden of Disease Study 2023
  (GBD 2023) Results. Seattle, United States: Institute for Health Metrics and Evaluation (IHME),
  2024. Available from https://vizhub.healthdata.org/gbd-results/.

## `raw/ihme_gbd2023_all_causes/` (first exploration, all causes)

- **Files:** `IHME-GBD_2023_DATA-91e6e136-1.csv` (full precision) and `table_exports/` (36
  `gbd_results_*.csv` files, values rounded to 2 decimals), plus `citation.txt`
- **From:** IHME GBD Results tool
- **Downloaded:** 2026-11-15
- **Query:** Deaths; Rate; 204 countries; 2023; Male / Female; 5-year age groups + All ages +
  Age-standardized; 36 causes
- **Note:** the table exports are rounded, so small rates show as 0.00.
- **License / cite:** as above

## `raw/who_gsrrs2023/`

- **File:** `gsrrs23-indicators-for-participating-countries-or-territories.xlsx`
  (sheets: `Indicators`, 173 rows x 228 columns; `Notes`)
- **From:** WHO Global status report on road safety 2023. TODO: add the exact download URL.
- **Downloaded:** 2026-11-17
- **License:** TODO: check the terms on the WHO page.
- **Cite:** TODO
