import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Analysis App")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data.head())

    if st.checkbox("Show summary statistics"):
        st.write(data.describe())

    if st.checkbox("Plot histogram"):
        st.write(data.hist(bins=10, figsize=(10, 5)))
        st.pyplot()

    if st.checkbox("Plot bar chart"):
        categorical_column = st.selectbox("Select a categorical column", data.columns.tolist())
        st.write(data.groupby(categorical_column).size().plot(kind='bar'))
        st.pyplot()
else:
    st.write("Please upload a CSV file")