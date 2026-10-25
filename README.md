# SQL E-commerce Analysis with DuckDB

Analyze the Online Retail transaction data with Python and DuckDB SQL. The current script calculates transaction-line revenue as `Quantity * UnitPrice`, country summaries, and monthly totals using parsed invoice dates.

## Important metric caveat

The current revenue calculation is a **line-value sum**, not a fully reconciled net-sales measure: the script does not consistently exclude cancelled invoices, returned quantities, or non-positive quantities/prices. Treat reported totals and country shares as exploratory until those rules are implemented and validated. Document the currency based on the source dataset metadata.

## Contents

- `data/data.csv` — source dataset (check its source and license before redistribution).
- `sql_analysis.py` — DuckDB SQL workflow.
- `results/revenue_by_country.csv` — generated country aggregation.
- `results/monthly_revenue.csv` — generated monthly aggregation.

## Run

Python 3.10+ recommended.

```bash
python -m pip install duckdb pandas
python sql_analysis.py
```

Run from the repository root. The script expects `data/data.csv` and writes outputs under `results/`.

## Current analyses

- Row count and dataset preview
- Total line-value revenue
- Revenue by country
- Monthly line-value trend with two attempted date formats

The README intentionally does not claim top-product, top-customer, or cancellation analysis as completed outputs until those queries are present and tested.

## Recommended next improvement

Add explicit cancellation/return rules, report invalid/unparsed dates, document the data source and currency, and test SQL aggregates against a small hand-calculated fixture.

## Author

Abdelhamid Moltazim · [GitHub profile](https://github.com/Moltazim-Data)
