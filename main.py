import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "sales_data.csv"
df = pd.read_csv(file_path)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Aggregate revenue by product
product_revenue = df.groupby("Product")["Revenue"].sum()

# Plot bar chart
plt.figure(figsize=(10, 5))
product_revenue.plot(kind="bar", color="skyblue", edgecolor="black")

plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Total Revenue per Product")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
