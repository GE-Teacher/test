import streamlit as st
import pandas as pd

# Text files

text_contents = '''
Foo, Bar
123, 456
789, 000
'''

# Different ways to use the API

st.download_button('Download CSV', text_contents, 'text/csv')
st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'

with open('data.csv', 't') as f:
	st.download_button('Download CSV', f)  # Defaults to 'text/plain'


# ---
# Binary files

binary_contents = b'whatever'

# Different ways to use the API

st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'

with open('myfile.zip', 'b') as f:
	st.download_button('Download Zip', f)  # Defaults to 'application/octet-stream'


# You can also grab the return value of the button,
# just like with any other button.

if st.download_button(...):
	st.write('Thanks for downloading!')