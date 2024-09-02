import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import os

# Load the historical rainfall data
df = pd.read_csv(os.path.join('dataset', 'rainfall_1901_2016_pak.csv'))
df.columns = df.columns.str.strip()
df['Month'] = df['Month'].map({
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
})

# Prepare the data for modeling
X = df[['Year', 'Month']]
y = df['Rainfall - (MM)']

degree = 2.5  # Adjusted degree for balance
poly = PolynomialFeatures(degree=int(degree))
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Predict future rainfall from 2017 to 2100
future_years = np.arange(2017, 2101)
future_data = []

for year in future_years:
    for month in range(1, 13):
        future_data.append([year, month])

future_df = pd.DataFrame(future_data, columns=['Year', 'Month'])
future_poly = poly.transform(future_df)
future_predictions = model.predict(future_poly)

historical_trend = np.mean(y[-10:]) - np.mean(y[:10])
yearly_trend = historical_trend / len(future_years)
cumulative_trend = np.arange(len(future_years)) * yearly_trend

np.random.seed(42)
seasonal_noise = np.sin(np.linspace(0, 12 * np.pi, len(future_predictions))) * 10
noise = np.random.normal(0, 15, size=future_predictions.shape) + seasonal_noise
future_predictions_adjusted = future_predictions + cumulative_trend.repeat(12) + noise

historical_df = df[['Year', 'Month', 'Rainfall - (MM)']]
future_df['Rainfall - (MM)'] = future_predictions_adjusted
combined_df = pd.concat([historical_df, future_df])

annual_rainfall = combined_df.groupby('Year')['Rainfall - (MM)'].sum()

plt.figure(figsize=(12, 6))
plt.plot(annual_rainfall.index, annual_rainfall.values, label="Annual Rainfall (MM)", color='blue')
plt.axvline(x=2016, color='red', linestyle='--', label="Start of Predictions")
plt.title("Rainfall Pattern from 1900 to 2100 with Balanced Peaks")
plt.xlabel("Year")
plt.ylabel("Total Rainfall (MM)")
plt.legend()
plt.grid(True)
plt.show()
