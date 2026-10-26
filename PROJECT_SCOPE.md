# HowLikely — Project Scope

**Working title:** How Likely Are You to Die Of...?  
**Repository / folder:** `howlikely`  
**Version:** 1.0 (MVP scope)  
**Status:** Planning

## 1. Vision

Build a free, mobile-friendly interactive website where visitors can explore annual mortality risks by country, age, sex, and cause of death. Unlike health-only tools, HowLikely gives external causes—road accidents, falls, drowning, poisoning, violence, and self-harm—equal prominence. It emphasizes clear, fast, understandable comparisons rather than dense statistical dashboards.

**Guiding principle:** Complex statistics underneath; a simple experience on top.

## 2. Audience and goals

- General public curious about risks and international differences.
- People who want to compare their demographic group across countries.
- Visitors who want to explore the geographic distribution of particular causes of death.
- Provide a useful public data exploration tool and a reproducible data-engineering / visualization portfolio project.

**Success target:** A visitor can enter a profile, see leading causes, select a comparison country, and explore the map in under 30 seconds.

## 3. MVP user journey

1. Select **country**, **age**, and **sex**.
2. Choose **All**, **Health**, or **External** causes.
3. See a concise leaderboard of the top five causes, expandable to ten.
4. Select a cause to see its **annual risk** (percentage and approximate “1 in N”).
5. Choose a **comparison country** to view side-by-side absolute and relative risks for the same demographic group.
6. Explore an **interactive world choropleth map** for the selected cause and demographic profile; click a country to change selection.

No registration is required.

## 4. Functional requirements

### 4.1 Demographic filters
- Searchable primary country selector.
- Optional searchable comparison-country selector.
- Age selector (0–100+ in the UI, mapped transparently to source-defined age bands).
- Sex selector based on source data categories; clearly label available categories.
- A consistent data year for each comparison.

### 4.2 Cause explorer
- Three modes: **All**, **Health**, **External**.
- Plain-language cause names mapped to standardized source codes.
- Searchable causes; expandable hierarchy from broad categories to specific causes.
- Top five causes shown by default; top ten on expansion.
- Avoid double-counting parent categories and their children.

**Health examples:** cardiovascular diseases, cancers, stroke, diabetes, infections, respiratory diseases, digestive diseases.  
**External examples:** road/transport accidents, falls, drowning, fires/burns, accidental poisoning, suicide/self-harm, homicide/assault, exposure to environmental forces, other injuries.

### 4.3 Risk display
- Annual cause-specific mortality rate per 100,000 people in the selected demographic group.
- Annual percentage and approximate 1-in-N equivalent.
- Optional share of deaths, explicitly distinguished from annual risk.
- Data year, source, and estimate/uncertainty information accessible without clutter.
- Never describe a demographic rate as an individualized prediction.

### 4.4 Country comparison
- Side-by-side risk for primary and comparison countries.
- Absolute difference and relative rate ratio, only when the denominator is valid.
- Identical age group, sex, cause, year, and estimation methodology.
- Clearly indicate missing data and avoid false precision.

### 4.5 World map
- Global country-level choropleth for selected cause, age, sex, and year.
- Target all countries and territories supported by the selected global source (GBD 2023 candidate: approximately 204; exact coverage to be verified).
- Hover/tap for country, annual rate, and year.
- Click to select a country; search, zoom, pan, reset.
- Legend, accessible colors, and neutral styling for missing data.
- Compare rates, **not raw death totals**; offer age-standardized rates for all-age comparisons.
- Harmonize country identifiers and map boundaries; document unmatched territories.

### 4.6 Accessibility and performance
- Responsive mobile and desktop layouts.
- Keyboard-accessible controls, readable labels, and non-color-only distinctions.
- Precomputed/cached queries where practical.
- Target typical filter responses under two seconds on normal connections.
- No personal profiles or account creation.

## 5. Data strategy

### Candidate sources
- **Primary candidate:** IHME Global Burden of Disease (GBD) 2023, for harmonized international cause-specific estimates.
- **Alternative / validation:** WHO Global Health Estimates and WHO Mortality Database.
- **Map boundaries:** Natural Earth or a suitably licensed GeoJSON dataset.
- **Population denominators:** Prefer population estimates consistent with the mortality source.

### Feasibility gate (before committing to implementation)
- Confirm country/territory coverage and identifiers.
- Confirm age-group, sex, year, and cause granularity.
- Confirm access, permitted download, attribution, publication, and redistribution terms.
- Confirm that the chosen source distinguishes external causes sufficiently.
- Validate representative examples (Moldova, Romania, Germany) against published estimates.
- Determine handling for countries with modeled rather than directly observed data.

**Rule:** No invented country values. Missing or non-comparable data are shown as unavailable.

## 6. Statistical methodology

For a defined country × year × age group × sex × cause:

`annual risk (%) = (cause-specific deaths / corresponding population) × 100`

`deaths per 100,000 = (cause-specific deaths / corresponding population) × 100,000`

`1 in N ≈ population / cause-specific deaths` (when deaths > 0)

- Use matched population denominators and source-defined age bands.
- Label results as population-level annual estimates, not personal forecasts.
- Use the same definitions and years for direct comparisons.
- Avoid mixing crude and age-standardized rates.
- Respect cause hierarchy so grouped categories sum correctly without double counting.
- Expose uncertainty where provided; suppress misleading ratios for zero, missing, or unstable values.
- A simple rate is an approximation of annual probability; note any methodological differences where relevant.

## 7. Proposed technology

| Layer | Candidate stack |
|---|---|
| Frontend | React + TypeScript + Tailwind CSS |
| Charts | Recharts |
| Map | MapLibre GL JS + suitable geographic boundaries |
| Backend | Python + FastAPI |
| ETL | Python + pandas or Polars |
| Analytics storage | DuckDB + Parquet |
| Tests | pytest + Vitest |
| Version control | Git + GitHub |
| Deployment | Vercel (frontend) + Python API host |

Technology choices may be simplified after a small performance and data-access proof of concept.

## 8. Suggested repository structure

```text
howlikely/
├── README.md
├── PROJECT_SCOPE.md
├── frontend/
│   └── ...
├── backend/
│   └── ...
├── data/
│   ├── README.md
│   └── sample/
├── pipelines/
│   └── ...
├── tests/
│   └── ...
├── docs/
│   └── ...
└── .gitignore
```

Do not commit large restricted source datasets, credentials, or personal information. Record data provenance and licenses in `data/README.md`.

## 9. Delivery phases

| Phase | Deliverable | Rough full-time effort |
|---|---|---|
| 1. Data feasibility | Access, licensing, granularity, representative sample | 1 week |
| 2. Data engineering | Reproducible ETL, cause mapping, validated rates | 1–2 weeks |
| 3. Backend | Filter, leaderboard, comparison, and map APIs | 1 week |
| 4. Frontend | Mobile UI, cause explorer, world map, comparison | 2–3 weeks |
| 5. Quality and launch | Statistical checks, usability, deployment, documentation | 1 week |

**Indicative total:** 6–8 weeks of focused full-time work, contingent on data access and licensing. Part-time development will take longer.

## 10. Out of scope for v1

- Individual medical diagnosis or personalized clinical risk scoring.
- Lifetime cause-specific death probabilities or future-risk forecasting.
- Lifestyle questionnaires and personal health records.
- AI chatbot.
- Real-time accident or death feeds.
- Subnational maps.
- User accounts and native mobile apps.
- Detailed historical trends and shareable image exports (possible v2 features).

## 11. Key risks

| Risk | Mitigation |
|---|---|
| Data license prohibits redistribution | Verify terms before publishing; use a permitted alternative or deployment strategy |
| Some countries/causes lack estimates | Show missing data clearly |
| Model uncertainty varies by country | Surface uncertainty and provenance |
| Age bands differ from user-selected age | Map to published bands and label them |
| Different country age structures distort comparison | Offer age-standardized all-age comparisons |
| Map mismatches / disputed boundaries | Use consistent geographic IDs and documented map conventions |
| Users confuse relative with absolute risk | Always display absolute annual rates alongside ratios |
| Excessive interface complexity | Progressive disclosure; top five causes first |

## 12. MVP acceptance criteria

- [ ] Global coverage matches all available countries and territories in the chosen source.
- [ ] Age, sex, country, and cause filters work.
- [ ] Health, External, and All views are available.
- [ ] Leading causes and annual mortality risks are displayed accurately.
- [ ] Comparison country can be selected and results use matching definitions.
- [ ] World map updates by cause and demographic filters; country selection works from the map.
- [ ] Data source, year, missingness, and uncertainty are communicated.
- [ ] Calculations are validated with automated tests and selected external benchmarks.
- [ ] Mobile and desktop usability are verified.
- [ ] Public deployment and GitHub documentation are complete.

## 13. Next immediate action

**Complete the data feasibility spike before building the UI.** Obtain a small, legally usable mortality sample covering Moldova, Romania, and Germany across several age groups, both sexes, and selected health/external causes. Validate the calculated rates and confirm that the same structure scales to global coverage.

---

*HowLikely is an exploratory public statistics tool. Results describe population-level mortality patterns and are not individual medical predictions.*
