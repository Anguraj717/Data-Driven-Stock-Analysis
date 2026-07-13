import pandas as pd
import os

INPUT_FILE = "data/master_stock_data_features.csv"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 60)
print("ANALYSIS 1 - TOP GREEN & RED STOCKS")
print("=" * 60)

# Load dataset
df = pd.read_csv(INPUT_FILE)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort by stock and date
df = df.sort_values(["Ticker", "date"])

# Calculate yearly return
summary = (
    df.groupby("Ticker")
      .agg(
          First_Close=("close", "first"),
          Last_Close=("close", "last"),
          Sector=("sector", "first")
      )
      .reset_index()
)

summary["Yearly_Return_%"] = (
    (summary["Last_Close"] - summary["First_Close"])
    / summary["First_Close"]
) * 100

# Top 10 gainers
top_green = summary.sort_values(
    by="Yearly_Return_%",
    ascending=False
).head(10)

# Top 10 losers
top_red = summary.sort_values(
    by="Yearly_Return_%",
    ascending=True
).head(10)

# Save results
top_green.to_csv(
    os.path.join(OUTPUT_FOLDER, "top_10_green_stocks.csv"),
    index=False
)

top_red.to_csv(
    os.path.join(OUTPUT_FOLDER, "top_10_red_stocks.csv"),
    index=False
)

print("\nTOP 10 GREEN STOCKS")
print(top_green)

print("\nTOP 10 RED STOCKS")
print(top_red)

print("\nResults saved successfully.")