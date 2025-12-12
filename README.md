# SQL-ecommerce-analysis
Beginner SQL analysis project using an E-commerce Sales dataset.
# 🛒 SQL E-commerce Analysis (DuckDB)

This project analyzes an e-commerce transactions dataset using **SQL** (via **DuckDB**) to compute key business metrics such as revenue, top-performing countries, and monthly revenue trends.

---

## 📌 Project Goals
- Load and query a large CSV dataset using SQL
- Calculate total revenue
- Rank countries by revenue
- Build a monthly revenue trend (handling real-world messy date formats)

---

## 🛠 Tools Used
- Python 3
- DuckDB (SQL engine)
- Git & GitHub

---

## 📁 Project Structure

```
sql-ecommerce-analysis/
│── data/
│ └── data.csv
│── results/
│ ├── revenue_by_country.csv
│ └── monthly_revenue.csv
│── sql_analysis.py
└── README.md
```

---

## 📊 Key Results
- **Total revenue:** ~9.75 million
- **Total transactions:** 541,909
- **Top country:** United Kingdom (~84% of revenue)
- **Seasonality:** Revenue peaks in late 2010 and early 2011

---

## 🔍 Analysis Performed
- Total revenue calculation
- Revenue by country
- Monthly revenue trend
- Top products by revenue
- Top customers by revenue
- Cancelled orders detection

---

## ⚠ Real-world Challenges Solved
- Non-UTF8 CSV encoding (`latin-1`)
- Mixed date formats (DD/MM and MM/DD)
- Large dataset performance using DuckDB

---

## ▶ How to Run

```bash
python3 -m pip install --user duckdb
python3 sql_analysis.py
```
---

## 👨‍💻 Author

Abdelhamid Moltazim

Junior Data Analyst — Vienna, Austria

GitHub: https://github.com/Moltazim-Data

