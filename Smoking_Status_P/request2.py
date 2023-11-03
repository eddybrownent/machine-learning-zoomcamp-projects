import requests
import pandas as pd

# Define the data for the person
data = {
    'age': 30.0,
    'height(cm)': 175.0,
    'weight(kg)': 85.0,
    'waist(cm)': 91.0,
    'eyesight(left)': 1.2,
    'eyesight(right)': 1.2,
    'hearing(left)': 1.0,
    'hearing(right)': 1.0,
    'systolic': 108.0,
    'relaxation': 72.0,
    'fasting blood sugar': 121.0,
    'Cholesterol': 175.0,
    'triglyceride': 358.0,
    'HDL': 46.0,
    'LDL': 57.0,
    'hemoglobin': 15.8,
    'Urine protein': 1.0,
    'serum creatinine': 1.0,
    'AST': 20.0,
    'ALT': 30.0,
    'Gtp': 105.0,
    'dental caries': 0.0
}

# Mean and Standard Deviation from your training data
mean = [44.12, 164.68, 
        38984.000000,38984.000000, 
        38984.000000, 38984.000000, 
        38984.000000, 38984.000000, 
        38984.000000, 38984.000000, 
        38984.000000, 38984.000000, 
        38984.000000, 38984.000000, 
        38984.000000, 38984.000000, 
        38984.000000, 38984.000000, 
        38984.000000, 38984.000000, 
        38984.000000, 38984.000000]  # Fill in the mean values for all features
std_dev = [12.063564, 9.187507,
           12.896581, 9.326798, 
           0.498527, 0.493813, 
           0.157246, 0.159703, 
           13.643529, 9.658734,
           14.617822, 42.883163, 
           1.566528, 0.402107,
           0.220621, 19.175595,
           31.309945, 49.693843, 
           0.410426,
           ]  # Fill in the standard deviation values

# Standardization
scaled_data = {}
for key, value in data.items():
    if key in mean and key in std_dev:
        scaled_data[key] = (value - mean[key]) / std_dev[key]
    else:
        scaled_data[key] = value

print(scaled_data)

# Make a POST request to the Flask API
response = requests.post("http://192.168.100.11:5000/predict", json=scaled_data)

# Check the response
if response.status_code == 200:
    result = response.json()  # The result from the API
    print(result)
else:
    print('Error:', response.status_code)
