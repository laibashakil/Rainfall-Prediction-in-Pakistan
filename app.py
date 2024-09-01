from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

df = pd.read_csv('dataset/rainfall_1901_2016_pak.csv')
df.columns = df.columns.str.strip()

month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
df['Month'] = df['Month'].map(month_map)

X = df[['Year', 'Month']]
y = df['Rainfall - (MM)']

model = LinearRegression()
model.fit(X, y)

@app.route('/')
def index():
    return "Rainfall Prediction API is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    year = data['Year']
    month = data['Month']
    
    month = month_map.get(month, month)  # Convert month name to number if necessary

    prediction = model.predict([[year, month]])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
