from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("best_model.pkl")
features = joblib.load("feature_names.pkl")

@app.route("/")
def home():
    return "API Running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_df = pd.DataFrame([data], columns=features)

    prob = model.predict_proba(input_df)[:, 1][0]
    prediction = "Malignant" if prob > 0.5 else "Benign"

    return jsonify({
        "prediction": prediction,
        "risk_score": round(prob * 100, 2)
    })