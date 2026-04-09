import streamlit as st
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.calibration import CalibratedClassifierCV

st.set_page_config(
    page_title="Breast Cancer XAI Dashboard",
    layout="wide"
)

try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

model = joblib.load("best_model.pkl")
features = joblib.load("feature_names.pkl")


st.markdown("<h1 style='text-align:center;'>🩺 Breast Cancer Prediction Dashboard</h1>", unsafe_allow_html=True)


st.sidebar.header("Input Patient Features")

user_input = {}
for feature in features:
    user_input[feature] = st.sidebar.number_input(feature, value=0.0)

input_df = pd.DataFrame([user_input])

if st.sidebar.button("Predict"):

    prob = model.predict_proba(input_df)[:, 1][0]
    prediction = "Malignant" if prob > 0.5 else "Benign"

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("Prediction Result")
        st.success(prediction)

    with col2:
        st.markdown("Risk Score")
        st.info(f"{round(prob * 100, 2)} %")

    # ---------------- SHAP ---------------- #
    st.markdown("---")
    st.markdown("Explainable AI (SHAP)")

    st.markdown("""
    SHAP explains how each feature contributed:
    - Positive → increases cancer risk  
    - Negative → decreases cancer risk  
    """)

    if isinstance(model, CalibratedClassifierCV):
        base_model = model.estimator
    else:
        base_model = model

    explainer = shap.TreeExplainer(base_model)

    shap_values = explainer.shap_values(input_df)

    if isinstance(shap_values, list):
        values = shap_values[1][0]
        base_value = explainer.expected_value[1]
    else:
        values = shap_values[0]
        base_value = explainer.expected_value

    explanation = shap.Explanation(
        values=values,
        base_values=base_value,
        data=input_df.iloc[0],
        feature_names=features
    )
    fig, ax = plt.subplots()
    shap.plots.waterfall(explanation, show=False)
    st.pyplot(fig)
    st.markdown("Top Influencing Features")

    importance_df = pd.DataFrame({
        "Feature": features,
        "Impact": values
    }).sort_values(by="Impact", key=abs, ascending=False).head(10)

    st.bar_chart(importance_df.set_index("Feature"))