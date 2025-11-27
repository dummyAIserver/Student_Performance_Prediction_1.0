import streamlit as st
import os

st.set_page_config(page_title="Student Predictor", layout="wide")

# Load CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="top-nav">
    <div class="top-nav-container">
        <div class="brand">
            <img src="logo.png" style="height:30px; margin-right:8px;">
            <b>Student Performance Predictor</b>
        </div>
        <div class="nav-links">
            <a href="📘_Predict_Marks">Predict</a>
            <a href="📊_Prediction_History">History</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.title("🎓 Welcome to Student Marks Predictor")
st.write("""
Use the sidebar or navigation bar to access:

### 👉 **Predict Marks**
Enter Attendance, Assignments, Internals → get final predicted marks.

### 👉 **View Prediction History**
See past predictions, download, or clear history.
""")
