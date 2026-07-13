import pandas as pd
import os

INPUT_FILE = "data/master_stock_data_features.csv"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 60)
print("MARKET SUMMARY")
print("=" * 60)

# Load data
df = pd.read_csv(INPUT_FILE)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["Ticker", "date"])

# First and last close price of each stock
summary = (
    df.groupby("Ticker")
      .agg(
          First_Close=("close", "first"),
          Last_Close=("close", "last")
      )
      .reset_index()
)

# Calculate yearly return
summary["Yearly_Return_%"] = (
    (summary["Last_Close"] - summary["First_Close"])
    / summary["First_Close"]
) * 100

# Green / Red count
green = (summary["Yearly_Return_%"] > 0).sum()
red = (summary["Yearly_Return_%"] < 0).sum()

# Average values
avg_close = df["close"].mean()
avg_volume = df["volume"].mean()

market_summary = pd.DataFrame({
    "Metric": [
        "Green Stocks",
        "Red Stocks",
        "Average Closing Price",
        "Average Volume"
    ],
    "Value": [
        green,
        red,
        round(avg_close, 2),
        round(avg_volume, 2)
    ]
})

print("\nMarket Summary\n")
print(market_summary)

market_summary.to_csv(
    os.path.join(OUTPUT_FOLDER, "market_summary.csv"),
    index=False
)

print("\nMarket Summary saved successfully.")