import streamlit as st
import pandas as pd

st.title("Data Analysis App")

st.write("Upload a CSV file to analyze its data")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data preview:")
    st.write(data.head())
    
    if st.checkbox("Show value counts"):
        st.write(data.iloc[:, -1].value_counts().plot(kind='bar'))
        st.pyplot()
        
    if st.checkbox("Show summary statistics"):
        st.write(data.describe())