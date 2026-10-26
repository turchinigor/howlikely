# Statistical methodology

Canonical definitions; implemented in `backend/src/howlikely/core/risk.py`.

For one country x year x age group x sex x cause cell:

- `annual risk (%) = deaths / population x 100`
- `deaths per 100,000 = deaths / population x 100,000`
- `1 in N ~ population / deaths` (only when deaths > 0)
- `rate ratio = primary rate / comparison rate` (suppressed when the comparison rate is zero or missing)

Rules:

- Use matched population denominators and source-defined age bands.
- Compare only identical age group, sex, cause, year, and estimation method.
- Never mix crude and age-standardized rates.
- Respect the cause hierarchy; never double-count a parent and its children.
- Expose uncertainty where the source provides it.
- Results are population-level annual estimates, not personal forecasts.
