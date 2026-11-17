# HowLikely: road safety

Who dies on the world's roads, and why? An exploration of road traffic deaths by country,
sex, and type of road user, using IHME Global Burden of Disease 2023 and WHO road safety data.

The findings go into a blog post with charts, and later into an interactive dashboard.

> All numbers are population-level annual rates. They are not personal predictions.

## Layout

```text
data/
  SOURCES.md     where every data file comes from
  raw/           downloaded files, untouched (not in git)
  processed/     cleaned tables (not in git)
notebooks/       analysis
src/howlikely/   reusable code (loading, cleaning, risk calculations)
tests/           tests for src/
```

## Setup

Open the repo in GitHub Codespaces. The dev container installs uv and runs `uv sync`.
Then download the data listed in [data/SOURCES.md](data/SOURCES.md) into `data/raw/`.

```bash
uv run pytest              # run tests
uv run ruff format .       # format code
uv run ruff check .        # lint
uv add <package>           # add a dependency (--dev for tools)
```

In notebooks, pick the `.venv` kernel.
