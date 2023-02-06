import streamlit as st
import requests

API_KEY = "your_api_key_here"

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

st.title("Weather App")

location = st.text_input("Enter a location")
if location:
    data = get_weather(location)
    if data["cod"] == 200:
        st.write(f"Temperature in {location}: {data['main']['temp']}°C")
    else:
        st.write("Location not found")
