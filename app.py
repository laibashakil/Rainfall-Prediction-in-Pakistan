from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

df = pd.read_csv(os.path.join('dataset', 'rainfall_1901_2016_pak.csv'))
df.columns = df.columns.str.strip()

month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
df['Month'] = df['Month'].map(month_map)

X = df[['Year', 'Month']]
y = df['Rainfall - (MM)'] 

degree = 2.5  # Adjusted degree for balance
poly = PolynomialFeatures(degree=int(degree))
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Historical trend calculation
historical_trend = np.mean(y[-10:]) - np.mean(y[:10])
future_years = np.arange(2017, 2101)
yearly_trend = historical_trend / len(future_years)
cumulative_trend = np.arange(len(future_years)) * yearly_trend

# @app.route('/')
# def index():
#     return "Rainfall Prediction API is running."

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    year = data['Year']
    month = data['Month']
    
    month = month_map.get(month, month)

    input_data = pd.DataFrame([[year, month]], columns=['Year', 'Month'])
    input_poly = poly.transform(input_data)

    base_prediction = model.predict(input_poly)[0]
    
    year_index = year - 2017
    if year_index < len(cumulative_trend):
        adjusted_prediction = base_prediction + cumulative_trend[year_index]
    else:
        adjusted_prediction = base_prediction

    np.random.seed(42)
    seasonal_noise = np.sin(np.pi * month / 6) * 10
    noise = np.random.normal(0, 15) + seasonal_noise

    final_prediction = adjusted_prediction + noise
    
    return jsonify({'prediction': final_prediction})

if __name__ == '__main__':
    app.run(debug=True)
