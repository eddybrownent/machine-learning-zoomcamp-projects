import pickle

from flask import Flask
from flask import request
from flask import jsonify


def load(filename):
    with open(filename, 'rb') as file_in:
        return pickle.load(file_in)

dv = load('dv.bin')
model = load('/model1.bin')

app = Flask('credit')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform(client)
    y_pred = model.predict_proba(X)[0, 1]
    get_credit = y_pred >= 0.5

    result = {
        'get_credit_prob': float(y_pred),
        'get_credit': bool(get_credit),

        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9616)