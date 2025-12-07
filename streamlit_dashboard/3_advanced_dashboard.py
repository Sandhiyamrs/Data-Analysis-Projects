"""
Streamlit advanced dashboard demo (run: streamlit run advanced_dashboard.py)
Requires: streamlit, pandas
"""
import streamlit as st
import pandas as pd
import numpy as np

def load_data():
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=100),
        "sales": np.random.randint(100,500,100),
        "category": np.random.choice(["A","B","C"],100)
    })

def main():
    st.title("Advanced Dashboard")
    df = load_data()
    st.line_chart(df.set_index("date")["sales"])
    cat = st.selectbox("Category", df['category'].unique())
    st.write(df[df.category==cat].describe())

if __name__=="__main__":
    main()
