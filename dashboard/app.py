"""
Streamlit dashboard for live motor fault predictions.
Run with: streamlit run dashboard/app.py
"""

import streamlit as st
import pandas as pd
import joblib
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ml"))
from feature_extraction import build_fused_feature_vector, simulate_signal

MODEL_PATH = "ml/model.pkl"

st.set_page_config(page_title="Motor Fault Diagnosis", layout="centered")
st.title("Motor Fault Diagnosis — Live Prediction")
st.caption("Sensor fusion of vibration (MPU6050) + current (ACS712) signatures")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    bundle = load_model()
    model, scaler = bundle["model"], bundle["scaler"]
    model_loaded = True
except FileNotFoundError:
    model_loaded = False
    st.warning("No trained model found yet. Run ml/train_model.py first.")

fault_option = st.selectbox(
    "Simulate signal (replace with live ESP32 serial/MQTT feed later)",
    ["healthy", "bearing", "imbalance", "misalignment"]
)

if st.button("Run Prediction") and model_loaded:
    vib, cur = simulate_signal(fault_type=fault_option)
    features = build_fused_feature_vector(vib, cur)
    X = pd.DataFrame([features])
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]

    st.subheader(f"Predicted condition: **{prediction}**")
    st.line_chart(vib[:200], height=200)
    st.caption("Vibration signal (first 200 samples)")
    st.line_chart(cur[:200], height=200)
    st.caption("Current signal (first 200 samples)")