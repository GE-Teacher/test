import streamlit as st
import openai

openai.api_key = "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"

st.title("Word Definition Game")

def generate_word():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Define the word: ',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response['choices'][0]['text']
    word = message.split(":")[1].strip()
    definition = message.split(":")[2].strip()
    return word, definition

word, definition = generate_word()

st.write("What is the definition of the word: `%s`?" % word)

user_answer = st.text_input("Enter your answer here:")

if user_answer.lower() == definition.lower():
    st.write("Correct!")
else:
    st.write("Incorrect. The definition of `%s` is: `%s`." % (word, definition))