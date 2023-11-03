import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import precision_score


# Create a StandardScaler instance
scaler = StandardScaler()


# Load your training data (e.g., 'train.csv')
df = pd.read_csv('train_dataset.csv')


# Removing duplicate rows

print("Number of duplicate rows: ", df[df.duplicated() == True].shape[0])
print(f"Rows in original Dataframe: {df.shape[0]}")

data = df.drop_duplicates()

print(f"Dataframe rows after removing duplicates: {data.shape[0]}")

# Define the features you want to scale (exclude the target variable)
features_to_scale = data.columns.drop(['smoking'])

# Apply the scaling to the selected features
data[features_to_scale] = scaler.fit_transform(data[features_to_scale])

# Separate features (X) and target (y)
X = data.drop(columns=['smoking'], axis=1)
y = data['smoking']

# Split the data into training and validation sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train your SVM model
model = SVC(C=1, kernel='rbf')  # Modify with your best hyperparameters
model.fit(X_train, y_train)

# Evaluate the best model on the testing set
y_pred = model.predict(X_test)
precision = precision_score(y_test, y_pred)

print(f"Precision on Testing Data: {precision:.4f}")

# Evaluate the model on the validation set
accuracy = model.score(X_test, y_test)
print(f'Validation Accuracy: {accuracy:.2f}')

# Save the trained SVM model to a file using joblib
joblib.dump(model, 'final_svm_model.pkl')

print('SVM Model saved as final_svm_model.pkl')

