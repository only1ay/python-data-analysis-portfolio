
import pandas as pd
import matplotlib.pyplot as plt

# Sample retail sales dataset
data = {
    "Date": [
        "2026-01-05", "2026-01-12", "2026-01-18",
        "2026-02-03", "2026-02-14", "2026-02-20",
        "2026-03-02", "2026-03-11", "2026-03-25",
        "2026-04-04", "2026-04-15", "2026-04-22"
    ],
    "Product": [
        "Laptop", "Phone", "Headphones",
        "Laptop", "Phone", "Tablet",
        "Headphones", "Laptop", "Tablet",
        "Phone", "Headphones", "Laptop"
    ],
    "Quantity": [2, 5, 8, 1, 4, 3, 10, 2, 5, 6, 7, 1],
    "Unit_Price": [450000, 250000, 35000, 450000,
                   250000, 180000, 35000, 450000,
                   180000, 250000, 35000, 450000],
    "Region": [
        "Lagos", "Ogun", "Oyo", "Lagos",
        "Ogun", "Abuja", "Oyo", "Lagos",
        "Abuja", "Ogun", "Oyo", "Lagos"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# Explore the dataset
print("FIRST FIVE RECORDS")
print(df.head())

print("\nDATASET INFORMATION")
df.info()

# Calculate total revenue
total_revenue = df["Revenue"].sum()
print("\nTOTAL REVENUE:", total_revenue)

# Sales by product
product_sales = df.groupby("Product")["Revenue"].sum()
print("\nREVENUE BY PRODUCT")
print(product_sales.sort_values(ascending=False))

# Sales by region
region_sales = df.groupby("Region")["Revenue"].sum()
print("\nREVENUE BY REGION")
print(region_sales.sort_values(ascending=False))

# Monthly sales
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\nMONTHLY REVENUE")
print(monthly_sales)

# Visualise product revenue
product_sales.sort_values().plot(
    kind="bar",
    title="Revenue by Product",
    xlabel="Product",
    ylabel="Revenue"
)

plt.tight_layout()
plt.show()
