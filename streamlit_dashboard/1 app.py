import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../datasets/dataset1.csv')

st.title("📊 Sales Dashboard")

st.line_chart(df['sales'])

st.write("Summary:")
st.write(df.describe())
