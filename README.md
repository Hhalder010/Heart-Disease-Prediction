# Heart Disease Prediction Project

## 🫀 Overview
This project predicts the 10-year risk of future coronary heart disease (CHD) using a machine learning model trained on the Framingham Heart Study dataset. It includes both a Jupyter notebook for data analysis/modeling and a Flask web application for user-friendly risk prediction.

---

## Link
https://p9s10hwn-5000.inc1.devtunnels.ms/

---

## 🚩 Problem Statement
World Health Organization estimates 12 million deaths occur worldwide every year due to heart diseases. Early prognosis of cardiovascular diseases can help in making lifestyle decisions for high-risk patients and reduce complications. This project aims to pinpoint the most relevant risk factors and predict overall risk using logistic regression.

---

## 💡 Solution
- **Classification Goal:** Predict whether a patient has a 10-year risk of future coronary heart disease (CHD).
- **Approach:** Logistic Regression Model for binary classification.
- **Web App:** A modern Flask-based web interface for instant risk prediction.

---

## 📊 Data Information
- **Dataset:** Framingham Heart Study (available in this repository as `framingham.csv`)
- **Records:** 4,000+ patients, 15 attributes
- **Source:** [Kaggle - Framingham Heart Study](https://www.kaggle.com/datasets/)

### **Features in the Dataset:**
- **Demographic:**
  - `sex`: male or female
  - `age`: age of the patient
  - `education`: 1=some high school, 2=high school diploma/GED, 3=some college/vocational, 4=college degree
- **Behavioral:**
  - `currentSmoker`: current smoker (yes/no)
  - `cigsPerDay`: cigarettes smoked per day
- **Medical History:**
  - `BPMeds`: on blood pressure medication
  - `prevalentStroke`: previous stroke
  - `prevalentHyp`: hypertensive
  - `diabetes`: diabetes
- **Physical Exam:**
  - `totChol`: total cholesterol
  - `sysBP`: systolic blood pressure
  - `diaBP`: diastolic blood pressure
  - `BMI`: body mass index
  - `heartRate`: heart rate
  - `glucose`: glucose level
- **Target:**
  - `TenYearCHD`: 10-year risk of CHD (0/1)

---

## 🧑‍🔬 Data Science Workflow
1. Importing required libraries
2. Importing and reading the dataset
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Data Visualization (correlation matrix, pairplot, countplots)
6. Data Modeling
    - Feature/target separation
    - Train/test split
    - Model training (Logistic Regression)
    - Prediction and evaluation (accuracy, classification report, confusion matrix)

---

## 🌐 Web App Features
- User-friendly web interface (Flask)
- Instant heart disease risk prediction (Low/High Risk)
- Modern UI with popups and animations
- Input validation and error handling

---

## 🏗️ Project Structure
```
├── app.py                        # Flask web application
├── model/
│   └── heart_disease_model.pkl   # Trained ML model
├── static/                       # CSS, images, etc.
├── templates/                    # HTML templates
├── requirements.txt              # Python dependencies
├── Heart_Disease_Prediction.ipynb# Jupyter notebook (EDA & modeling)
├── framingham.csv                # Dataset
└── README.md                     # Project documentation
```

---

## 🚀 How to Run the Web App Locally

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Hhalder010/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction
   ```
2. **(Optional) Create a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask app:**
   ```sh
   python app.py
   ```
5. **Open your browser and go to:**
   [http://localhost:5000](http://localhost:5000)

---

## 🏥 Model Information
- **Algorithm:** Logistic Regression
- **Trained on:** Framingham Heart Study dataset
- **Input features:** gender, age, education, smoking status, blood pressure, cholesterol, BMI, heart rate, glucose, and more
- **Model file:** `model/heart_disease_model.pkl`

---

## 📋 Example Usage
1. Fill in the form with your health and lifestyle details.
2. Click "Predict Risk".
3. A popup will display your risk prediction (Low Risk or High Risk).

---

## 🛠️ Dependencies
- Flask
- joblib
- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn

Install all dependencies with:
```sh
pip install -r requirements.txt
```

---

## 📸 Screenshots
_Add screenshots of the web app and notebook outputs here (optional)_

---

## 🙏 Credits
- Built by Hrithik Halder
- Model and dataset: Framingham Heart Study
- UI inspired by modern health dashboards

---

## 📄 License
This project is for educational purposes. 
