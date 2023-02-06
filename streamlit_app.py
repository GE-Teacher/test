import streamlit as st
import random

st.title("Guess the Number Game")
st.write("Guess a number between 1 and 100 and see if you can guess correctly.")

number = random.randint(1, 100)

guess = st.number_input("Enter your guess:")

if guess == number:
    result = "Correct!"
else:
    result = "Wrong! The number was " + str(number)

st.write("Result:", result)