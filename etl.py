import pandas as pd

# Extract
df = pd.read_csv("sales_data.csv")

print("Original Data")
print(df)

# Transform
df = df.dropna()

df["Amount"] = df["Amount"].astype(int)

# Analysis
total_sales = df["Amount"].sum()

city_sales = df.groupby("City")["Amount"].sum()

print("\nTotal Sales:", total_sales)

print("\nCity Wise Sales")
print(city_sales)

# Load
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nETL Process Completed") 