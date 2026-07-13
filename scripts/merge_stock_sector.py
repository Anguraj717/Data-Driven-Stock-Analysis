import os
import pandas as pd

# Folder containing stock CSV files
CSV_FOLDER = "data/csv"

# Sector mapping file
SECTOR_FILE = "data/csv/sector_data.csv"

# Output file
OUTPUT_FILE = "data/master_stock_data.csv"

# Read sector data
sector_df = pd.read_csv(SECTOR_FILE)
print("\nSector Data:")
print(sector_df.head())

print("\nSector Columns:")
print(sector_df.columns.tolist())

# Keep only Symbol and Sector columns
sector_df = sector_df[["Symbol", "sector"]]

# Extract actual stock symbol after ':'
sector_df["Ticker"] = sector_df["Symbol"].str.split(":").str[-1].str.strip()

# Keep only Ticker and sector
sector_df = sector_df[["Ticker", "sector"]]

all_data = []

# Read every stock CSV
for file in sorted(os.listdir(CSV_FOLDER)):

    if not file.endswith(".csv"):
        continue

    if file == "sector_data.csv":
        continue

    file_path = os.path.join(CSV_FOLDER, file)

    df = pd.read_csv(file_path)

    # Merge with sector data
    df = df.merge(sector_df, on="Ticker", how="left")

    all_data.append(df)

# Combine all stocks
master_df = pd.concat(all_data, ignore_index=True)

# Save master dataset
master_df.to_csv(OUTPUT_FILE, index=False)

print("=" * 60)
print("MASTER DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print(f"\nTotal Rows : {len(master_df)}")
print(f"Total Columns : {len(master_df.columns)}")

print("\nColumns:")
print(master_df.columns.tolist())

print("\nFirst 5 Rows:")
print(master_df.head())