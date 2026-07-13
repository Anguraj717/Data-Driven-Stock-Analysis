import pandas as pd
import os

INPUT_FILE = "data/master_stock_data_features.csv"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 60)
print("MONTHLY TOP GAINERS & LOSERS")
print("=" * 60)

# Load data
df = pd.read_csv(INPUT_FILE)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Extract month
df["YearMonth"] = df["date"].dt.to_period("M").astype(str)

results = []

for month in sorted(df["YearMonth"].unique()):

    month_df = df[df["YearMonth"] == month].sort_values(["Ticker", "date"])

    summary = (
        month_df.groupby("Ticker")
                .agg(
                    First_Close=("close", "first"),
                    Last_Close=("close", "last")
                )
                .reset_index()
    )

    summary["Monthly_Return_%"] = (
        (summary["Last_Close"] - summary["First_Close"])
        / summary["First_Close"]
    ) * 100

    # Top 5 gainers
    gainers = summary.sort_values(
        "Monthly_Return_%",
        ascending=False
    ).head(5)

    gainers["Month"] = month
    gainers["Type"] = "Gainer"

    # Top 5 losers
    losers = summary.sort_values(
        "Monthly_Return_%",
        ascending=True
    ).head(5)

    losers["Month"] = month
    losers["Type"] = "Loser"

    results.append(gainers)
    results.append(losers)

final_df = pd.concat(results, ignore_index=True)

print(final_df.head(20))

final_df.to_csv(
    os.path.join(OUTPUT_FOLDER, "monthly_gainers_losers.csv"),
    index=False
)

print("\nSaved successfully.")