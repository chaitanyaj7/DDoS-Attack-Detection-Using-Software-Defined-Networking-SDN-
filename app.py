import streamlit as st
import pandas as pd
import joblib

# ===== App Configuration =====
st.set_page_config(page_title="DDoS Attack Detector", page_icon="🛡️", layout="centered")

# ===== Load Model Files =====
model = joblib.load('svm_ddos.pkl')
scaler = joblib.load('scaler_ddos.pkl')
columns = joblib.load('columns_ddos.pkl')

# ===== Page Title =====
st.title("🛡️ DDoS Attack Detection System")
st.markdown("---")
st.markdown("### 🔍 Enter Network Traffic Features Below")

# ===== Feature Input Section =====
with st.form("input_form"):
    inputs = {}
    cols_per_row = 2  # two inputs per row for better layout

    for i, col in enumerate(columns):
        if i % cols_per_row == 0:
            cols = st.columns(cols_per_row)
        inputs[col] = cols[i % cols_per_row].number_input(f"{col}", value=0.0, step=0.1)

    submitted = st.form_submit_button("🚀 Predict")

# ===== Prediction Section =====
if submitted:
    df = pd.DataFrame([inputs])
    X_scaled = scaler.transform(df)
    pred = model.predict(X_scaled)[0]
    proba = model.predict_proba(X_scaled)[0][1] if hasattr(model, "predict_proba") else None

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    if pred == 1:
        st.success("✅ **Normal Traffic Detected!**")
    else:
        st.error("⚠️ **DDoS Attack Detected! Take Action Immediately!**")

    if proba is not None:
        st.progress(int(proba * 100))
        st.info(f"**Attack Probability:** {proba:.2%}")

    st.markdown("---")
    st.caption("Model: SVM | Developed by Chaitanya Jamdar 🧠")

