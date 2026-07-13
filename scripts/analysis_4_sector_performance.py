import pandas as pd
import os

INPUT_FILE = "data/master_stock_data_features.csv"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 60)
print("SECTOR PERFORMANCE ANALYSIS")
print("=" * 60)

# Load data
df = pd.read_csv(INPUT_FILE)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort by ticker and date
df = df.sort_values(["Ticker", "date"])

# Calculate yearly return for each stock
stock_returns = (
    df.groupby("Ticker")
      .agg(
          First_Close=("close", "first"),
          Last_Close=("close", "last"),
          Sector=("sector", "first")
      )
      .reset_index()
)

stock_returns["Yearly_Return_%"] = (
    (stock_returns["Last_Close"] - stock_returns["First_Close"])
    / stock_returns["First_Close"]
) * 100

# Average return by sector
sector_summary = (
    stock_returns.groupby("Sector")
                 .agg(
                     Average_Yearly_Return=("Yearly_Return_%", "mean"),
                     Number_of_Stocks=("Ticker", "count")
                 )
                 .reset_index()
                 .sort_values(
                     by="Average_Yearly_Return",
                     ascending=False
                 )
)

print("\nSector-wise Performance\n")
print(sector_summary)

sector_summary.to_csv(
    os.path.join(OUTPUT_FOLDER, "sector_performance.csv"),
    index=False
)

print("\nSector performance saved successfully.")