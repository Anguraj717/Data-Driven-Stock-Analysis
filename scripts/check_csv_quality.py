import os
import pandas as pd

CSV_FOLDER = "data/csv"

print("=" * 70)
print("STOCK DATA VALIDATION REPORT")
print("=" * 70)

csv_files = sorted(
    [f for f in os.listdir(CSV_FOLDER)
     if f.endswith(".csv") and f != "sector_data.csv"]
)

print(f"\nStock CSV Files Found : {len(csv_files)}")

for csv_file in csv_files:

    file_path = os.path.join(CSV_FOLDER, csv_file)

    df = pd.read_csv(file_path)

    print("\n" + "-" * 60)
    print(f"File: {csv_file}")

    print(f"Rows       : {len(df)}")
    print(f"Columns    : {len(df.columns)}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")

print("\n" + "=" * 60)
print("QUALITY CHECK COMPLETED")
print("=" * 60)