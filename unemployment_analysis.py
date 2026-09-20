import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert date
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Convert unemployment rate to numeric
df["Estimated Unemployment Rate (%)"] = pd.to_numeric(
    df["Estimated Unemployment Rate (%)"], errors="coerce"
)

print("Unemployment Analysis")
print("---------------------")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# Average unemployment rate by region
region_avg = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

print("\nAverage Unemployment Rate by Region:")
print(region_avg.sort_values(ascending=False))

# Bar chart
region_avg.sort_values(ascending=False).plot(
    kind="bar",
    figsize=(12, 5)
)

plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Trend over time
monthly = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean()

monthly.plot(figsize=(12, 5))

plt.title("Unemployment Rate Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()