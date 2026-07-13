import os
import yaml
import pandas as pd
from collections import defaultdict

RAW_DATA_FOLDER = "data/raw_yaml"
OUTPUT_FOLDER = "data/csv"

stock_data = defaultdict(list)

# Loop through each month folder
for month_folder in sorted(os.listdir(RAW_DATA_FOLDER)):

    month_path = os.path.join(RAW_DATA_FOLDER, month_folder)

    # Skip if it is not a folder
    if not os.path.isdir(month_path):
        continue

    print(f"Processing folder: {month_folder}")

    # Loop through all YAML files in the current month folder
    for yaml_file in sorted(os.listdir(month_path)):

        if yaml_file.endswith(".yaml"):

            yaml_path = os.path.join(month_path, yaml_file)

            with open(yaml_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            print(f"\nReading: {yaml_file}")
            print(f"Number of records: {len(data)}")

            # Read every stock record in the YAML file
            for record in data:

                ticker = record["Ticker"]

                stock_data[ticker].append(record)

    print("\n===================================")
print("YAML Extraction Completed!")
print("===================================")

print(f"Total Stocks Found: {len(stock_data)}")

print("\nFirst 5 Stock Names:")

for ticker in list(stock_data.keys())[:5]:
    print(ticker)

    # Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Create one CSV file for each stock
for ticker, records in stock_data.items():

    df = pd.DataFrame(records)

    # Sort by date
    df = df.sort_values("date")

    # Save CSV
    output_file = os.path.join(OUTPUT_FOLDER, f"{ticker}.csv")

    df.to_csv(output_file, index=False)

print("\n===================================")
print("CSV files created successfully!")
print(f"Total CSV Files: {len(stock_data)}")
print("===================================")