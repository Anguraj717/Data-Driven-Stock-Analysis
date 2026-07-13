import pandas as pd
import os

INPUT_FILE = "data/master_stock_data_features.csv"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 60)
print("STOCK PRICE CORRELATION")
print("=" * 60)

# Load data
df = pd.read_csv(INPUT_FILE)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Create pivot table
pivot_df = df.pivot(index="date", columns="Ticker", values="close")

# Correlation matrix
correlation_matrix = pivot_df.corr()

print("\nCorrelation Matrix Shape:")
print(correlation_matrix.shape)

print("\nFirst 5 Rows:")
print(correlation_matrix.head())

# Save output
correlation_matrix.to_csv(
    os.path.join(OUTPUT_FOLDER, "stock_correlation_matrix.csv")
)

print("\nCorrelation matrix saved successfully.")