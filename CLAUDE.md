# CLAUDE.md

Road safety analysis project. Findings go into a blog post (charts from the notebooks) and later
a Streamlit dashboard (`app.py`, not built yet).

The user is learning data analysis. Keep code simple and beginner-readable: no extra layers,
no defensive code for cases that can't happen, short comments only where needed.

## Layout

- `data/raw/<source>/`: untouched downloads, git-ignored. Provenance in `data/SOURCES.md`.
- `data/processed/`: cleaned tables, git-ignored.
- `notebooks/`: analysis. Run from `notebooks/`, so paths start with `../data/`.
- `src/howlikely/`: code reused across notebooks. `risk.py` has rate / 1-in-N helpers.
- `tests/`: pytest for `src/`.

## Commands

```bash
uv run pytest
uv run ruff check . && uv run ruff format --check .
```

CI runs those three. Clear notebook outputs before committing (they contain source data).

## Data rules

- Never invent values. Show missing data as missing.
- Compare countries with age-standardized rates, never crude "All ages" rates.
- Don't add or average rates across groups. Combine counts, or use the source's "Both" sex.
- Don't double-count a parent cause with its children (Road injuries contains Pedestrian, etc.).
- Never commit data files. Record every new source in `data/SOURCES.md`.
