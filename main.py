from flask import Flask, jsonify, request
import joblib
import os
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP Requests', ['endpoint'])

MODEL_PATH = "model.joblib"
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

@app.route('/health', methods=['GET'])
def health():
    REQUEST_COUNT.labels(endpoint='/health').inc()
    return jsonify({"status": "HEALTHY"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    REQUEST_COUNT.labels(endpoint='/predict').inc()
    if not model:
        return jsonify({"error": "Model not loaded"}), 500
    
    data = request.get_json()
    features = data.get("features", [])
    prediction = model.predict([features]).tolist()
    return jsonify({"prediction": prediction})

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
