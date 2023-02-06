import streamlit as st
import pandas as pd

# Load the data into a pandas dataframe
df = pd.read_csv("addresses.csv")

st.title("Data Browser")

# Show the data as a table
st.dataframe(df)

# Add a search bar
search = st.text_input("Search")

# Show only the rows that match the search
if search:
    df = df[df["column_name"].str.contains(search, case=False)]
    st.dataframe(df)