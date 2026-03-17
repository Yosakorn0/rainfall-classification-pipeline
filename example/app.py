from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model once at startup
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html') # This serves the frontend

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Convert input to 2D array for the model
    features = np.array([[data['value']]])
    prediction = model.predict(features)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
