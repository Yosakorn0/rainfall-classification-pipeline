import picklecl
import numpy as np
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Load trained model (created by src/train.py)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json(force=True)

    required = ['Humidity3pm', 'Rainfall', 'Pressure3pm', 'Cloud3pm']
    if not all(k in payload for k in required):
        return jsonify({'error': 'Missing one or more required features'}), 400

    values = [float(payload[k]) for k in required]
    X = np.array(values, dtype=float).reshape(1, -1)

    prediction = int(model.predict(X)[0])
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)