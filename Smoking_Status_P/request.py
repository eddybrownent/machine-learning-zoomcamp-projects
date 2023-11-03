import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Read the data from a CSV file
df = pd.read_csv('test_dataset.csv')

# Removing duplicate rows

print("Number of duplicate rows: ", df[df.duplicated() == True].shape[0])
print(f"Rows in original Dataframe: {df.shape[0]}")

data = df.drop_duplicates()

print(f"Dataframe rows after removing duplicates: {data.shape[0]}")


# Create a StandardScaler instance
scaler = StandardScaler()

# Extract the numerical features from the test data (exclude the target variable)
numerical_features = data.columns


# Apply the scaling to the selected features
data[numerical_features] = scaler.fit_transform(data[numerical_features])

# Iterate through the rows of the DataFrame
for index, row in data.iterrows():
    # Convert the current row to a dictionary
    prediction_data = row.to_dict()

    # Make a POST request to the Flask API
    response = requests.post("http://192.168.100.11:5000/predict", json=prediction_data)

    # Check the response
    if response.status_code == 200:
        result = response.json()  # The result from the API
        print(f"Prediction for Row {index}: {result}")
    else:
        print(f'Error for Row {index}: {response.status_code}')

