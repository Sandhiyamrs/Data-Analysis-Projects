"""
Utilities for Streamlit dashboard (caching, loaders)
"""
import pandas as pd
import streamlit as st

@st.cache_data
def load_csv(path):
    return pd.read_csv(path)
