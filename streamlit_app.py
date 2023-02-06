import streamlit as st
import pandas as pd

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

st.write(df)

if st.button('Save as CSV'):
    st.write("Saving data...")
    df.to_csv('data.csv', index=False)
    st.write("Data saved!")