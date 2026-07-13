import pandas as pd

sector_df = pd.read_csv("data/csv/sector_data.csv")
stock_df = pd.read_csv("data/csv/SBIN.csv")

print("===== SECTOR DATA =====")
print(sector_df.head())
print("\nColumns:")
print(sector_df.columns.tolist())

print("\n===== STOCK DATA =====")
print(stock_df.head())
print("\nColumns:")
print(stock_df.columns.tolist())

print("\nFirst Sector Symbol:")
print(repr(sector_df.loc[0, "Symbol"]))

print("\nFirst Stock Ticker:")
print(repr(stock_df.loc[0, "Ticker"]))