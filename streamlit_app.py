import streamlit as st

username = st.text_input("Enter your username")
age = st.slider("Enter your age", min_value=0, max_value=100, value=18, step=1)

st.write("Hello, ", username)
st.write("Your age is: ", age)