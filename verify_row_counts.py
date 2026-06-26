import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("bluestock_mf.db")

# CSV files and corresponding database tables
tables = {
    "fund_master": "data/raw/01_fund_master.csv",
    "nav_history": "data/processed/nav_history_clean.csv",
    "scheme_performance": "data/processed/scheme_performance_clean.csv",
    "investor_transactions": "data/processed/investor_transactions_clean.csv",
    "aum_by_fund_house": "data/raw/03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "data/raw/04_monthly_sip_inflows.csv",
    "category_inflows": "data/raw/05_category_inflows.csv",
    "industry_folio_count": "data/raw/06_industry_folio_count.csv",
    "portfolio_holdings": "data/raw/09_portfolio_holdings.csv",
    "benchmark_indices": "data/raw/10_benchmark_indices.csv"
}

print("=" * 75)
print(f"{'Table':30} {'CSV Rows':10} {'DB Rows':10} Status")
print("=" * 75)

for table, csv_path in tables.items():
    csv_df = pd.read_csv(csv_path)
    csv_rows = len(csv_df)

    db_rows = pd.read_sql_query(
        f"SELECT COUNT(*) AS count FROM {table}",
        conn
    )["count"][0]

    status = "✅ MATCH" if csv_rows == db_rows else "❌ MISMATCH"

    print(f"{table:30} {csv_rows:<10} {db_rows:<10} {status}")

conn.close()