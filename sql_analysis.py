import duckdb

# Load data from CSV
con = duckdb.connect()

df = con.execute("""
    SELECT *
    FROM read_csv_auto('data/data.csv')
""").df()

print("Dataset loaded:")
print(df.head())

# Example queries
print("\n🔹 Total number of orders:")
print(con.execute("""
    SELECT COUNT(*) AS total_orders
    FROM read_csv_auto('data/data.csv')
""").fetchdf())

print("\n🔹 Total revenue:")
print(con.execute("""
    SELECT SUM(UnitPrice * Quantity) AS revenue
    FROM read_csv_auto('data/data.csv')
""").fetchdf())

print("\n🔹 Top 10 products by sales:")
print(con.execute("""
    SELECT Description, SUM(Quantity) AS total_sold
    FROM read_csv_auto('data/data.csv')
    GROUP BY Description
    ORDER BY total_sold DESC
    LIMIT 10
""").fetchdf())
