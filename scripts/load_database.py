import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# -------------------------------
# Create Database Folder
# -------------------------------
db_folder = Path("data/db")
db_folder.mkdir(parents=True, exist_ok=True)

# -------------------------------
# Create SQLite Database
# -------------------------------
engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

# -------------------------------
# Load Cleaned CSV Files
# -------------------------------
nav = pd.read_csv("data/processed/nav_history_clean.csv")

transactions = pd.read_csv(
    "data/processed/transactions_clean.csv"
)

performance = pd.read_csv(
    "data/processed/performance_clean.csv"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

# Store in SQLite

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")

print("\nTables Created:")
print("- dim_fund")
print("- fact_nav")
print("- fact_transactions")
print("- fact_performance")