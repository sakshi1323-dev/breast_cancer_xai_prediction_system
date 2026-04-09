from flask import Flask, request, jsonify
import joblib
import pandas as pd
import shap
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("best_model.pkl")
features = joblib.load("feature_names.pkl")


explainer = shap.TreeExplainer(model)

@app.route("/")
def home():
    return "API Running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        input_df = pd.DataFrame([data], columns=features)

        prob = model.predict_proba(input_df)[:, 1][0]
        prediction = "Malignant" if prob > 0.5 else "Benign"

        shap_values = explainer(input_df)

        feature_importance = {}
        for i, feature in enumerate(features):
            feature_importance[feature] = float(shap_values.values[0][i])

        return jsonify({
            "prediction": prediction,
            "risk_score": round(prob * 100, 2),
            "feature_importance": feature_importance
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)