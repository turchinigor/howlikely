# CLAUDE.md

HowLikely: public site showing annual mortality risk by country, age, sex, and cause.
Scope: [PROJECT_SCOPE.md](PROJECT_SCOPE.md). Methodology: [docs/methodology.md](docs/methodology.md).

## Current phase

Phase 1, data feasibility spike (PROJECT_SCOPE.md section 13). Get a small, legally usable sample
for Moldova, Romania, and Germany before building the UI. `frontend/` is not scaffolded on purpose.

## Commands

```bash
pytest                                  # tests (tests/backend, tests/pipelines)
ruff check . && ruff format --check .   # lint + format
mypy                                    # strict type-check
uvicorn howlikely.main:app --reload     # API, http://localhost:8000/docs
howlikely-etl all                       # ETL stages (stubs)
pre-commit run --all-files
```

CI (`.github/workflows/ci.yml`) runs ruff, mypy, and pytest. Keep all of them green.

## Layout

- `backend/src/howlikely/`: FastAPI app (`main.py`, routes under `api/routes/`, mounted at `/api/v1`)
  and `core/`, which holds domain logic shared with the ETL.
- `pipelines/src/howlikely_etl/`: ETL, raw sources -> Parquet + DuckDB in `data/processed/`.
- Settings come from `HOWLIKELY_*` env vars or `.env` (see `.env.example`).

## Rules

- Never invent country values. Show missing or non-comparable data as unavailable.
- Rates are population-level annual estimates. Never present them as individual predictions.
- Compare only identical age group, sex, cause, year, and method. Never mix crude and
  age-standardized rates. Don't double-count a parent cause together with its children.
- Never commit raw or restricted datasets (`data/raw|interim|processed` are git-ignored).
  Record every source's provenance and license in `data/README.md` before using it.
- Record significant technology or data-source decisions as ADRs in `docs/adr/`.
- Python: 3.12, strict mypy, ruff at line length 100, full type hints.
