import duckdb

con = duckdb.connect()
csv_path = "data/data.csv"

def q(sql: str):
    return con.execute(sql).fetchdf()

print("🔹 Preview of the dataset:\n")
print(q(f"""
    SELECT *
    FROM read_csv_auto('{csv_path}', encoding='latin-1', ignore_errors=true)
    LIMIT 5
"""))

print("\n🔹 Number of rows in the dataset:")
print(q(f"""
    SELECT COUNT(*) AS n_rows
    FROM read_csv_auto('{csv_path}', encoding='latin-1', ignore_errors=true)
"""))

print("\n🔹 Total revenue:")
print(q(f"""
    SELECT SUM(Quantity * UnitPrice) AS total_revenue
    FROM read_csv_auto('{csv_path}', encoding='latin-1', ignore_errors=true)
"""))

print("\n🔹 Top 10 countries by revenue:")
print(q(f"""
    SELECT Country,
           SUM(Quantity * UnitPrice) AS revenue
    FROM read_csv_auto('{csv_path}', encoding='latin-1', ignore_errors=true)
    GROUP BY Country
    ORDER BY revenue DESC
    LIMIT 10
"""))

print("\n🔹 Monthly revenue (first 12 months):")
print(q(f"""
    WITH parsed AS (
        SELECT
            COALESCE(
                try_strptime(InvoiceDate, '%d/%m/%Y %H:%M'),
                try_strptime(InvoiceDate, '%m/%d/%Y %H:%M')
            ) AS ts,
            Quantity,
            UnitPrice
        FROM read_csv_auto('{csv_path}', encoding='latin-1', ignore_errors=true)
    )
    SELECT
        strftime(ts, '%Y-%m') AS year_month,
        SUM(Quantity * UnitPrice) AS revenue
    FROM parsed
    WHERE ts IS NOT NULL
    GROUP BY year_month
    ORDER BY year_month
    LIMIT 12
"""))

print("\n🎉 SQL analysis finished.")

# Save results to CSV files
q("""
    SELECT Country,
           SUM(Quantity * UnitPrice) AS revenue
    FROM read_csv_auto('data/data.csv', encoding='latin-1', ignore_errors=true)
    GROUP BY Country
    ORDER BY revenue DESC
""").to_csv("results/revenue_by_country.csv", index=False)

q("""
    WITH parsed AS (
        SELECT
            COALESCE(
                try_strptime(InvoiceDate, '%d/%m/%Y %H:%M'),
                try_strptime(InvoiceDate, '%m/%d/%Y %H:%M')
            ) AS ts,
            Quantity,
            UnitPrice
        FROM read_csv_auto('data/data.csv', encoding='latin-1', ignore_errors=true)
    )
    SELECT
        strftime(ts, '%Y-%m') AS year_month,
        SUM(Quantity * UnitPrice) AS revenue
    FROM parsed
    WHERE ts IS NOT NULL
    GROUP BY year_month
    ORDER BY year_month
""").to_csv("results/monthly_revenue.csv", index=False)

print("✅ Results saved to /results folder")

