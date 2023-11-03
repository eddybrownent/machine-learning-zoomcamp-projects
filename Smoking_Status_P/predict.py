from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("final_svm_model.pkl")

# Define a dictionary to map JSON keys to column names
key_to_column = {
    'age': 'age',
    'height(cm)': 'height(cm)',
    'weight(kg)': 'weight(kg)',
    'waist(cm)': 'waist(cm)',
    'eyesight(left)': 'eyesight(left)',
    'eyesight(right)': 'eyesight(right)',
    'hearing(left)': 'hearing(left)',
    'hearing(right)': 'hearing(right)',
    'systolic': 'systolic',
    'relaxation': 'relaxation',
    'fasting blood sugar': 'fasting blood sugar',
    'Cholesterol': 'Cholesterol',
    'triglyceride': 'triglyceride',
    'HDL': 'HDL',
    'LDL': 'LDL',
    'hemoglobin': 'hemoglobin',
    'Urine protein': 'Urine protein',
    'serum creatinine': 'serum creatinine',
    'AST': 'AST',
    'ALT': 'ALT',
    'Gtp': 'Gtp',
    'dental caries': 'dental caries'
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
