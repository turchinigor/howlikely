# HowLikely

**How likely are you to die of...?** A free, mobile-friendly site for exploring annual mortality
risk by country, age, sex, and cause of death, with external causes (road accidents, falls,
drowning, violence, self-harm) given equal weight to health causes.

> Results describe population-level annual mortality rates. They are not individual medical predictions.

See [PROJECT_SCOPE.md](PROJECT_SCOPE.md) for the full MVP scope.

## Repository layout

```text
howlikely/
├── backend/src/howlikely/     FastAPI app + shared domain logic (risk calculations)
├── pipelines/src/howlikely_etl/  ETL: raw sources -> validated Parquet / DuckDB
├── frontend/                  React + TypeScript + Tailwind UI (not scaffolded yet)
├── data/                      Local data (raw/processed are git-ignored); see data/README.md
├── tests/                     pytest suites (backend/, pipelines/)
├── docs/                      Methodology, architecture, decision records
└── pyproject.toml             Python project, dependencies, tool config
```

## Development setup (Windows)

Virtual environment lives outside the repo at `C:\venvs\howlikely` (Python 3.12).

```powershell
C:\venvs\howlikely\Scripts\Activate.ps1
pip install -e ".[dev]"
pre-commit install
```

Common commands:

```powershell
pytest                                  # run tests
ruff check . ; ruff format .            # lint + format
mypy                                    # type-check
uvicorn howlikely.main:app --reload     # API at http://localhost:8000/docs
howlikely-etl all                       # run ETL stages
```

Copy `.env.example` to `.env` to override settings.

## Status

Phase 1: data feasibility spike (see PROJECT_SCOPE.md section 13).
