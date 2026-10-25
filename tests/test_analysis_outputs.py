from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_source_has_expected_online_retail_fields():
    path = ROOT / "data" / "data.csv"
    assert path.exists()
    sample = pd.read_csv(path, encoding="latin-1", nrows=10)
    required = {"InvoiceNo", "Quantity", "UnitPrice", "InvoiceDate", "Country"}
    assert required.issubset(sample.columns)

def test_generated_result_files_have_expected_columns():
    country_path = ROOT / "results" / "revenue_by_country.csv"
    monthly_path = ROOT / "results" / "monthly_revenue.csv"
    assert country_path.exists() and monthly_path.exists()
    country = pd.read_csv(country_path)
    monthly = pd.read_csv(monthly_path)
    assert {"Country", "revenue"}.issubset(country.columns)
    assert {"year_month", "revenue"}.issubset(monthly.columns)
    assert country["revenue"].notna().all()
    assert monthly["year_month"].notna().all()
