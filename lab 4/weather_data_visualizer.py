import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---- Load CSV ----
df = pd.read_csv("weather_data.csv")

# ---- Data Cleaning ----
df.columns = [c.strip() for c in df.columns]
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# Keep only relevant columns if present
keep = ['Date']
for col in ['Temperature', 'Rainfall', 'Humidity']:
    if col in df.columns:
        keep.append(col)
df = df[keep]

# Fill missing numeric values with column mean
for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].mean())

# Add Year and Month columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# ---- Statistical Analysis ----
print("\nDaily Temperature Stats:")
if 'Temperature' in df.columns:
    arr = df['Temperature'].to_numpy()
    print("Mean:", np.mean(arr))
    print("Min:", np.min(arr))
    print("Max:", np.max(arr))
    print("Std Dev:", np.std(arr, ddof=1))

if 'Rainfall' in df.columns:
    monthly_rain = df.set_index('Date').resample('M')['Rainfall'].sum()
    print("\nMonthly Rainfall (first 5 rows):")
    print(monthly_rain.head())

# ---- Export cleaned dataset ----
df.to_csv("cleaned_weather.csv", index=False)
print("\nCleaned CSV saved as cleaned_weather.csv")

# ---- Plots ----
if 'Temperature' in df.columns:
    plt.figure(figsize=(10, 4))
    plt.plot(df['Date'], df['Temperature'])
    plt.title("Daily Temperature Line Plot")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig("daily_temp_line.png")
    plt.close()

if 'Rainfall' in df.columns:
    plt.figure(figsize=(8, 4))
    df.set_index('Date').resample('M')['Rainfall'].sum().plot(kind='bar')
    plt.title("Monthly Rainfall Bar Plot")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.tight_layout()
    plt.savefig("monthly_rainfall_bar.png")
    plt.close()

if 'Temperature' in df.columns and 'Humidity' in df.columns:
    plt.figure(figsize=(6, 5))
    plt.scatter(df['Temperature'], df['Humidity'], alpha=0.6)
    plt.title("Humidity vs Temperature Scatter")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Humidity (%)")
    plt.tight_layout()
    plt.savefig("humidity_vs_temp_scatter.png")
    plt.close()

print("\nPlots Saved:")
print("- daily_temp_line.png")
print("- monthly_rainfall_bar.png")
print("- humidity_vs_temp_scatter.png (if humidity exists)")

print("\n--- Program Finished ---")
