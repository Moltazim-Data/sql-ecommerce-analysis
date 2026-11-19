# E-commerce Revenue Analysis with DuckDB SQL

An exploratory SQL analysis of the Online Retail transaction dataset using DuckDB. The workflow calculates line-value revenue, country summaries and monthly totals from invoice dates.

## Project files
- `data/data.csv` — source dataset; review its provenance and license before redistribution.
- `sql_analysis.py` — DuckDB analysis script.
- `results/revenue_by_country.csv` — country-level aggregation.
- `results/monthly_revenue.csv` — monthly aggregation.

## Run
Python 3.10+ recommended.
```bash
python -m pip install duckdb pandas
python sql_analysis.py
```
The script reads `data/data.csv` and writes result files under `results/`.

## Analysis
- Dataset size and preview
- Total line-value sum
- Country-level revenue summary
- Monthly trend using invoice dates

## Metric scope
Revenue is currently calculated as `Quantity × UnitPrice`. The analysis does not yet fully reconcile cancellations, returns, or negative/non-positive quantities and prices. Treat totals as exploratory, not net sales. Confirm currency and source metric definitions before drawing conclusions.


## Author
Abdelhamid Moltazim · [GitHub](https://github.com/Moltazim-Data) · [Portfolio](https://moltazimdata.com)
