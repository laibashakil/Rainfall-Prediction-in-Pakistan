
# 🌧️ Rainfall Prediction System

**A simple yet powerful web application that predicts monthly rainfall based on historical data using machine learning.**
![image](https://github.com/user-attachments/assets/6deb20d7-29b1-4c49-9708-76d5e3a94d7f)

## 📊 Dataset

The dataset used in this project includes historical monthly rainfall data from 1901 to 2016. The dataset was sourced from [Open Data Pakistan](https://opendata.com.pk/dataset/rainfall-in-pakistan) and contains the following columns:

-   **Year**: The year of the observation.
-   **Month**: The month of the observation.
-   **Rainfall (MM)**: The recorded rainfall in millimeters.

## 🤖 Machine Learning Model

The machine learning model is a **Linear Regression** model built using Scikit-Learn. The model is trained on the historical dataset to predict rainfall for a given year and month. Key steps include:

1.  **Data Preprocessing**: Handling missing data, converting categorical data (months) into numerical values.
2.  **Model Training**: Fitting the linear regression model on the training data.
3.  **Prediction**: Using the trained model to predict rainfall based on the input year and month.

## 🛠️ Tech Stack

### Frontend:
-   **HTML5**: The structure of the web page.
-   **CSS3**: Styling for a modern, responsive design.
-   **JavaScript**: Handles user interaction and API calls.

### Backend:
-   **Python 3.10**: The core programming language used for building the backend.
-   **Flask**: A lightweight WSGI web application framework used to build the RESTful API.

### Machine Learning:
-   **Scikit-Learn**: Used for building and training the linear regression model.
-   **Pandas**: Data manipulation and analysis.
-   **Numpy**: Supports large, multi-dimensional arrays and matrices.

### Deployment:
-   **Vercel**: For deploying the web application.

## 💻 Usage

### Accessing the Application

-   Visit the deployed application at https://rainfall-prediction-in-pakistan.vercel.app.
-   Enter the year and month for which you want to predict rainfall.
-   Click the "Predict Rainfall" button to see the results.

### API Usage

The application also exposes a RESTful API that can be used to get predictions programmatically.
![image](https://github.com/user-attachments/assets/b24d5be7-7e56-43be-80bd-a491d958dccf)

**Endpoint**: `/predict`

**Method**: `POST`

**Payload Example**:

`{
  "Year": 2029,
  "Month": "September"
}` 

**Response Example**:

`{
  "prediction": 23.743647858123385
}`
