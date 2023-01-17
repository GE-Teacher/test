import streamlit as st

video_file = open('myimage.png', 'rb')
video_bytes = video_file.read()

st.image(video_bytes)