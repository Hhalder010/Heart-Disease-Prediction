from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('heart_disease_model_full.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    risk = None
    if request.method == 'POST':
        try:
            features = [
                int(request.form['gender']),
                int(request.form['age']),
                int(request.form['education']),
                int(request.form['currentSmoker']),
                int(request.form['cigsPerDay']),
                int(request.form['BPMeds']),
                int(request.form['prevalentStroke']),
                int(request.form['prevalentHyp']),
                int(request.form['diabetes']),
                int(request.form['totChol']),
                int(request.form['sysBP']),
                int(request.form['diaBP']),
                float(request.form['BMI']),
                int(request.form['heartRate']),
                int(request.form['glucose'])
            ]
            features_np = np.array(features).reshape(1, -1)
            prediction = model.predict(features_np)[0]
            risk = "Low Risk" if prediction == 0 else "High Risk"
        except Exception as e:
            risk = f"Error in input: {str(e)}"

    return render_template('index.html', risk=risk)

if __name__ == '__main__':
    app.run(debug=True)