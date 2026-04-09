# 🩺 Breast Cancer Prediction System with Explainable AI (XAI)

## Overview
This project is a **Machine Learning-based Breast Cancer Prediction System** that not only predicts whether a tumor is **Malignant or Benign**, but also explains the prediction using **Explainable AI (SHAP)**.

It helps improve trust and transparency in healthcare predictions by showing **how each feature contributes to the final decision**.


## Features
- Breast Cancer Prediction (Benign / Malignant)
- Risk Score (0–100%)
- Multiple ML Models Comparison
- Best Model Selection (XGBoost + Calibration)
- SHAP Explainability (Feature Contribution)
- Interactive UI using Streamlit
- Clean and User-Friendly Dashboard


## Tech Stack
-Programming Language:Python  
-Libraries: 
  - Pandas, NumPy  
  - Scikit-learn  
  - XGBoost  
  - SHAP (Explainable AI)  
  - Matplotlib, Seaborn  
- Frontend/UI:Streamlit  

## Project Structure
```bash
Breast_Cancer_XAI_and_Risk/
│
├── app.py                  # Streamlit dashboard
├── best_model.pkl          # Trained ML model
├── feature_names.pkl       # Feature list
├── requirements.txt        # Dependencies
├── README.md
│
├── notebooks/              # EDA & training
│   └── breast_cancer_analysis.ipynb
│
├── assets/                 # UI styling
│   └── style.css
```


## How to Run Locally

### 1.Clone the Repository
```bash
git clone https://github.com/sakshi1323-dev/breast_cancer_xai_prediction_system.git
cd breast_cancer_xai_prediction_system
2. Install Dependencies
pip install -r requirements.txt
3. Run the Application
streamlit run app.py

👉 The app will open in your browser automatically.

Model Details
Models Used:
Logistic Regression
Decision Tree
Random Forest
SVM
KNN
XGBoost

Best Model Selected: XGBoost
Accuracy optimized using training & evaluation
Probability Calibration applied (Isotonic Regression)
Risk score generated from calibrated probabilities
Explainable AI (XAI) – SHAP

This project uses SHAP (SHapley Additive exPlanations) to explain predictions.

✔ What SHAP does:
Shows feature contribution
Explains why prediction is Malignant or Benign
Improves model transparency

✔ Output includes:
SHAP Waterfall Plot
Feature Importance Ranking
Output Example
Prediction: Benign / Malignant
Risk Score: e.g., 78.45%
SHAP Explanation Graph
Top Influencing Features

Author
Sakshi Shelke
B.Tech ECE (AI/ML)







