import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Prediction History", layout="wide")

with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

HISTORY_FILE = "history.csv"

st.markdown('<div style="width:85%; margin:auto;">', unsafe_allow_html=True)
st.markdown('<div class="history-card">', unsafe_allow_html=True)

st.markdown('<h2 style="color:#214b9c; font-weight:700;">📊 Prediction History</h2>', unsafe_allow_html=True)

if os.path.exists(HISTORY_FILE):
    df = pd.read_csv(HISTORY_FILE)
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", csv, file_name="history.csv", mime="text/csv")

    with col2:
        if st.button("🗑 Clear History"):
            os.remove(HISTORY_FILE)
            st.success("History cleared. Refresh page.")
else:
    st.info("No prediction history yet.")

st.markdown("</div></div>", unsafe_allow_html=True)
