# sql-ecommerce-analysis
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

sql-ecommerce-analysis/
│── data/
│ └── data.csv
│── sql_analysis.py
└── README.md

---

## 🔍 Key Queries / Analysis
- Total number of rows
- Total revenue: `SUM(Quantity * UnitPrice)`
- Top 10 countries by revenue
- Monthly revenue trend using parsed timestamps

✅ Real-world fixes included:
- Non-UTF8 CSV encoding handled with `encoding='latin-1'`
- Mixed date formats handled using `try_strptime()` + `coalesce()`

---

## 📈 Results Snapshot
- Rows: **541,909**
- Total revenue: **~ 9.75M**
- Top country by revenue: **United Kingdom**
- Monthly revenue output produced successfully

---

## ▶️ How to Run
```bash
python3 -m pip install --user duckdb
python3 sql_analysis.py

👨‍💻 Author

Abdelhamid Moltazim
Junior Data Analyst — Vienna, Austria
GitHub: https://github.com/Moltazim-Data

