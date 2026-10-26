# Data

`raw/`, `interim/`, and `processed/` are git-ignored. Only small, redistributable files go in
`sample/`. Never commit restricted source datasets, credentials, or personal information.

| Folder | Contents |
|---|---|
| `raw/` | Unmodified downloads from sources, exactly as received |
| `interim/` | Cleaned / harmonized intermediate files |
| `processed/` | Final Parquet tables and the DuckDB database the API reads |
| `sample/` | Small, license-permitted samples for tests and demos |

## Provenance and licenses

Record every source here before using it.

| Source | Version / year | URL | License / terms | Redistribution allowed? | Retrieved |
|---|---|---|---|---|---|
| IHME GBD 2023 (candidate) | TBD | TBD | TBD | TBD | TBD |
| WHO Global Health Estimates (validation) | TBD | TBD | TBD | TBD | TBD |
| Natural Earth boundaries (candidate) | TBD | TBD | TBD | TBD | TBD |
