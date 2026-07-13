import pandas as pd
import os

INPUT_FILE = "data/master_stock_data_features.csv"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 60)
print("VOLATILITY ANALYSIS")
print("=" * 60)

# Load data
df = pd.read_csv(INPUT_FILE)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort by stock and date
df = df.sort_values(["Ticker", "date"])

# Calculate daily return
df["Daily_Return"] = (
    df.groupby("Ticker")["close"]
      .pct_change()
)

# Calculate volatility (standard deviation)
volatility = (
    df.groupby("Ticker")
      .agg(
          Volatility=("Daily_Return", "std"),
          Sector=("sector", "first")
      )
      .reset_index()
)

# Convert to percentage
volatility["Volatility_%"] = volatility["Volatility"] * 100

# Top 10 most volatile stocks
top10 = (
    volatility.sort_values(
        by="Volatility_%",
        ascending=False
    )
    .head(10)
)

print("\nTop 10 Most Volatile Stocks\n")
print(top10[["Ticker", "Sector", "Volatility_%"]])

top10.to_csv(
    os.path.join(OUTPUT_FOLDER, "top10_volatility.csv"),
    index=False
)

print("\nSaved successfully.")