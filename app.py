import streamlit as st
import pandas as pd

st.title("My Data Visualization Dashboard 📊")

# Read the CSV file directly (make sure it's in the same folder)
df = pd.read_csv("data.csv")

st.subheader("Data Preview")
st.write(df.head())

st.subheader("Summary Statistics")
st.write(df.describe())

st.subheader("Numeric Columns Chart")
st.bar_chart(df.select_dtypes(include='number'))
