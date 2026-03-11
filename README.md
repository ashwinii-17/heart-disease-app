# Heart Disease Prediction Web App

## Overview

This project is a **machine learning based web application** that predicts the risk of heart disease using patient health parameters.
The system uses a **Logistic Regression model** trained on the **Framingham Heart Study dataset** and provides predictions through a **Flask web interface**.

Users enter health-related information such as age, cholesterol level, blood pressure, BMI, heart rate, and glucose level. The application processes this data and predicts whether the person has a **high or low risk of heart disease**.

---

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML
* CSS
* JavaScript

---

## Dataset

The model is trained using the **Framingham Heart Study dataset**, which contains medical attributes related to cardiovascular health.

Target Variable:

* `TenYearCHD` → Indicates whether the patient has a **10-year risk of coronary heart disease**

Features used in the model:

* Age
* Gender (Male/Female)
* Total Cholesterol
* Systolic Blood Pressure
* Diastolic Blood Pressure
* Body Mass Index (BMI)
* Heart Rate
* Glucose Level

---

## Project Structure

```
heart_disease_app
│
├── app.py
├── train_model.py
├── framingham.csv
│
├── templates
│   └── index.html
│
└── static
    ├── style.css
    └── script.js
```

---

## How the System Works

1. The dataset is loaded and cleaned.
2. Missing values are replaced with the column mean.
3. Selected features are used to train a **Logistic Regression model**.
4. Input data from the user is standardized using **StandardScaler**.
5. The trained model predicts whether the user has a **high or low risk of heart disease**.
6. The result is displayed on the web interface with color indicators:

   * Green → Low Risk
   * Red → High Risk

---

## Installation

Clone the repository or download the project folder.

Install required libraries:

```
pip install flask pandas numpy scikit-learn
```

---

## Running the Project

Step 1 – Train the model (optional check)

```
python train_model.py
```

Step 2 – Run the Flask web application

```
python app.py
```

Step 3 – Open the application in your browser

```
http://127.0.0.1:5000
```

---

## Features

* Multi-step user input form
* Modern dark themed UI
* Machine learning prediction using Logistic Regression
* Data preprocessing and feature scaling
* Color-coded prediction results
* Responsive interface

---

## Future Improvements

* Add prediction probability score
* Add graphical risk meter visualization
* Deploy the application on cloud platforms (Heroku / Render)
* Use advanced models such as Random Forest or XGBoost

---

## Author

Ashwini
B.Tech – Computer Science Engineering (AI & ML)
