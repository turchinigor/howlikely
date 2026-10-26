# Architecture

```text
sources (GBD / WHO / Natural Earth)
   -> pipelines (howlikely_etl: extract -> transform -> load)
   -> data/processed/*.parquet + howlikely.duckdb
   -> backend (FastAPI, read-only queries, /api/v1/...)
   -> frontend (React + MapLibre, deployed on Vercel)
```

- `howlikely.core` holds domain logic used by both the API and the pipelines.
- The API is read-only; all heavy computation is precomputed by the ETL.
- Architecture decisions are recorded in `docs/adr/`.
