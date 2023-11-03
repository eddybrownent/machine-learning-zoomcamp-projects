from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("best_model.pkl")

# Define a dictionary to map JSON keys to column names
key_to_column = {
    'age': 'age',
    'height(cm)': 'height',
    'weight(kg)': 'weight',
    'waist(cm)': 'waist',
    'eyesight(left)': 'eyesight_left',
    'eyesight(right)': 'eyesight_right',
    'hearing(left)': 'hearing_left',
    'hearing(right)': 'hearing_right',
    'fasting blood sugar': 'fasting_blood_sugar',
    'Cholesterol': 'Cholesterol',
    'triglyceride': 'triglyceride',
    'HDL': 'HDL',
    'LDL': 'LDL',
    'hemoglobin': 'haemoglobin',
    'AST': 'AST',
    'ALT': 'ALT',
    'Gtp': 'Gtp',
    'Urine protein': 'urine_protein',
    'serum creatinine': 'serum_creatinine',
    'dental caries': 'dental_caries'
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = []

    for key, column_name in key_to_column.items():
        if column_name in data:
            features.append(data[column_name])

    prediction = model.predict([features])

    prediction_label = "Smoker" if prediction[0] == 1 else "Non-Smoker"

    return jsonify({"prediction": prediction_label})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
