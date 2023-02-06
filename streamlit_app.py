import streamlit as st
import pandas as pd
import hashlib

# Register a new user
def register():
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Save the new user to a database
    # In a real application, you would use a database library to do this
    df = pd.DataFrame({'Username': [username], 'Password': [hashed_password]})
    df.to_csv('users.csv', mode='a', index=False, header=False)
    st.success("User registered!")

# Log in to an existing account
def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    # Hash the password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username and password match a registered user
    # In a real application, you would use a database library to do this
    df = pd.read_csv('users.csv')
    if (df['Username'] == username).any() and (df['Password'] == hashed_password).any():
        st.success("Logged in as {}".format(username))
    else:
        st.error("Incorrect username or password")

def main():
    st.set_page_config(page_title="User Management", page_icon=":guardsman:", layout="wide")
    menu = ["Homepage", "Login", "Register"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Login":
        login()
    elif choice == "Register":
        register()
    else:
        st.write("Welcome to the User Management App")

if __name__ == '__main__':
    main()