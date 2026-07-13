import pandas as pd

df = pd.read_csv("data/master_stock_data_features.csv")

missing = df[df["sector"].isna()]

print("=" * 60)
print("STOCKS WITH MISSING SECTOR")
print("=" * 60)

print("Missing Rows:", len(missing))

print("\nAffected Tickers:")
print(missing["Ticker"].unique())