
# 🌧️ Rainfall Prediction System

A simple yet powerful web application that predicts monthly rainfall based on historical data using machine learning.

### Screenshot of App:
![image](https://github.com/user-attachments/assets/2527faac-7589-49b1-8601-69e788452723)

## 📊 Dataset

The dataset used in this project includes historical monthly rainfall data from 1901 to 2016. The dataset was sourced from [Open Data Pakistan](https://opendata.com.pk/dataset/rainfall-in-pakistan) and contains the following columns:

-   **Year**: The year of the observation.
-   **Month**: The month of the observation.
-   **Rainfall (MM)**: The recorded rainfall in millimeters.


## 🤖 Machine Learning Model

The machine learning model is based on **Polynomial Regression** with added custom trend analysis and noise to create realistic predictions. The model leverages historical data to predict rainfall for a given year and month, reflecting natural variability and gradual trends.

### Key Steps Include:

1.  **Data Preprocessing**:
    
    -   Handling missing data.
    -   Converting categorical data (months) into numerical values.
    -   Creating polynomial features to capture non-linear relationships.
2.  **Model Training**:
    
    -   The model is trained using a polynomial regression approach to fit the historical data more accurately than a simple linear regression.
3.  **Prediction**:
    
    -   Predictions include:
        -   Polynomial regression-based estimation.
        -   A custom cumulative trend based on historical patterns.
        -   Added noise to mimic natural variability and avoid unrealistic flat predictions.

### Visual Representation:

![image](https://github.com/user-attachments/assets/7f7934c4-1023-4b2c-b1fd-68ff5007d576)

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
![image](https://github.com/user-attachments/assets/c310153f-0804-4d51-b13a-635e12d7690c)
