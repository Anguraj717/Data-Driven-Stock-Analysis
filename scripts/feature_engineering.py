import pandas as pd

INPUT_FILE = "data/master_stock_data.csv"
OUTPUT_FILE = "data/master_stock_data_features.csv"

print("=" * 60)
print("FEATURE ENGINEERING STARTED")
print("=" * 60)

# Load data
df = pd.read_csv(INPUT_FILE)

print(f"\nRows Loaded : {len(df)}")
print(f"Columns     : {len(df.columns)}")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["Ticker", "date"])

print("\nData Sorted Successfully")

# -------------------------------------------------------
# Daily Return (%)
# -------------------------------------------------------

df["Daily_Return_%"] = (
    df.groupby("Ticker")["close"]
      .pct_change() * 100
)

print("✓ Daily Return calculated")

# -------------------------------------------------------
# Price Change
# -------------------------------------------------------

df["Price_Change"] = df["close"] - df["open"]

print("✓ Price Change calculated")


# -------------------------------------------------------
# High-Low Difference
# -------------------------------------------------------

df["High_Low_Diff"] = df["high"] - df["low"]

print("✓ High-Low Difference calculated")


# -------------------------------------------------------
# 5-Day Moving Average
# -------------------------------------------------------

df["MA_5"] = (
    df.groupby("Ticker")["close"]
      .transform(lambda x: x.rolling(5).mean())
)

print("✓ 5-Day Moving Average calculated")


# -------------------------------------------------------
# 20-Day Moving Average
# -------------------------------------------------------

df["MA_20"] = (
    df.groupby("Ticker")["close"]
      .transform(lambda x: x.rolling(20).mean())
)

print("✓ 20-Day Moving Average calculated")
# -------------------------------------------------------
# Save Feature Engineered Dataset
# -------------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\n" + "=" * 60)
print("FEATURE ENGINEERING COMPLETED")
print("=" * 60)

print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

print(f"\nSaved to : {OUTPUT_FILE}")