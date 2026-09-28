import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Basic data-quality checks
print("Rows:", len(df))
print("Missing values:")
print(df.isna().sum())
print("Duplicate order IDs:", df["order_id"].duplicated().sum())

# KPI summary
print("\nTotal revenue:", round(df["revenue"].sum(), 2))
print("Total orders:", df["order_id"].nunique())
print("Average order value:", round(df["revenue"].sum()/df["order_id"].nunique(), 2))

# Revenue by category
category_revenue = (
    df.groupby("category", as_index=False)["revenue"]
      .sum()
      .sort_values("revenue", ascending=False)
)
print("\nRevenue by category:")
print(category_revenue)

# Revenue by city
city_revenue = (
    df.groupby("city", as_index=False)["revenue"]
      .sum()
      .sort_values("revenue", ascending=False)
)
print("\nRevenue by city:")
print(city_revenue)

# Monthly trend
monthly = (
    df.assign(month=df["date"].dt.to_period("M").astype(str))
      .groupby("month", as_index=False)["revenue"]
      .sum()
)
print("\nMonthly revenue:")
print(monthly)

# Visualization
monthly.plot(x="month", y="revenue", kind="line", marker="o", legend=False)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue.png", dpi=150)
plt.show()
