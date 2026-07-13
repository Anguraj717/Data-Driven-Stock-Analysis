import pandas as pd
import mysql.connector

# -------------------------------
# MySQL Connection
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7171aa@@",
    database="stock_analysis"
)

cursor = conn.cursor()

# -------------------------------
# Load CSV
# -------------------------------
green_df = pd.read_csv("output/top_10_green_stocks.csv")
red_df = pd.read_csv("output/top_10_red_stocks.csv")

green_df["Stock_Type"] = "Green"
red_df["Stock_Type"] = "Red"

df = pd.concat([green_df, red_df], ignore_index=True)

print(df.head())

# -------------------------------
# Insert Data
# -------------------------------
for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO top_green_red_stocks
        (Ticker, First_Close, Last_Close, Sector,
         Yearly_Return_Percent, Stock_Type)

        VALUES (%s,%s,%s,%s,%s,%s)
    """,
    (
        row["Ticker"],
        row["First_Close"],
        row["Last_Close"],
        row["Sector"],
        row["Yearly_Return_%"],
        row["Stock_Type"]
    ))

conn.commit()

print("=================================")
print("Data Imported Successfully!")
print("=================================")

cursor.close()
conn.close()