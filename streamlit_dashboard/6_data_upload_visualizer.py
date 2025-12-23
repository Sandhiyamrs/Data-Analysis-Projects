import streamlit as st
import pandas as pd

file = st.file_uploader("Upload CSV")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    st.line_chart(df.select_dtypes(include='number'))
