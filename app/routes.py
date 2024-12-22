from flask import request, jsonify
from app import app
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load models
lr_model = joblib.load('app/models/best_logistic_regression_model.pkl')
rf_model = joblib.load('app/models/best_random_forest_model.pkl')
scaler = joblib.load('app/models/scaler.pkl')

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Server is running"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON
        data = request.json
        
        # Extract features
        features = np.array([
            data['destination_port'],
            data['flow_duration'],
            data['flow_bytes_per_s'],
            data['total_fwd_packets'],
            data['packet_length_mean']
        ]).reshape(1, -1)

        # Scale features
        scaled_features = scaler.transform(features)

        # Make predictions
        lr_prediction = lr_model.predict(scaled_features)[0]
        rf_prediction = rf_model.predict(scaled_features)[0]

        # Return response
        response = {
            "logistic_regression": "BENIGN" if lr_prediction == 0 else "ATTACK",
            "random_forest": "BENIGN" if rf_prediction == 0 else "ATTACK"
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/dashboard_data', methods=['GET'])
def dashboard_data():
    try:
        data = {
            "total_connections": 5000,
            "normal": 4800,
            "suspicious": 150,
            "attacks": 50,
            "charts": {
                "traffic_breakdown": [
                    {"type": "BENIGN", "count": 4800},
                    {"type": "SUSPICIOUS", "count": 150},
                    {"type": "ATTACK", "count": 50}
                ],
                "traffic_trend": [
                    {"timestamp": "10:00", "connections": 100},
                    {"timestamp": "10:05", "connections": 200},
                    {"timestamp": "10:10", "connections": 150}
                ]
            }
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400