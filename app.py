import streamlit as st
import pandas as pd

st.title("My First Streamlit App 🎉")

file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.write("### Data Preview", df.head())
    st.bar_chart(df.select_dtypes(include='number'))
