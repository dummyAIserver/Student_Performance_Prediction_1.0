import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

st.set_page_config(page_title="Predict Marks", layout="wide")

with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

MODEL_PATH = "model.pkl"
HISTORY_FILE = "history.csv"

model = pickle.load(open(MODEL_PATH, "rb"))

# UI Card Layout
st.markdown('<div class="center-area"><div class="stream-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">🎓 Student Final Marks Predictor</div>', unsafe_allow_html=True)

with st.form("predict_form"):
    attendance = st.number_input("Attendance (%)", 0.0, 100.0, placeholder="Enter attendance (0-100)")
    assignment = st.number_input("Assignment Score", 0.0, 100.0, placeholder="Enter attendance (0-20)")
    internal = st.number_input("Internal Marks", 0.0, 50.0, placeholder="Enter attendance (0-30)")
    submit = st.form_submit_button("Predict Marks")

st.markdown('</div></div>', unsafe_allow_html=True)

# Logic
if submit:
    x = np.array([[attendance, assignment, internal]])
    pred = round(float(model.predict(x)[0]), 2)

    # Result
    st.markdown(f'<div class="result-box">Predicted Final Marks: <b>{pred}</b></div>', unsafe_allow_html=True)

    # Save history
    row = pd.DataFrame([{
        "attendance": attendance,
        "assignment": assignment,
        "internal": internal,
        "prediction": pred
    }])

    if os.path.exists(HISTORY_FILE):
        row.to_csv(HISTORY_FILE, mode="a", header=False, index=False)
    else:
        row.to_csv(HISTORY_FILE, index=False)
