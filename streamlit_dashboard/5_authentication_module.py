import streamlit as st

def login():
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and pwd == "admin":
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

login()
