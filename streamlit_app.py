import pandas as pd
import git




import streamlit as st

def save_csv():
    # Code to save the DataFrame as a CSV file


    # Create a DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    
    # Save the DataFrame as a CSV file
    df.to_csv('data.csv', index=False)
    
    # Code to push the CSV file to GitHub
    # Clone the repository
    repo = git.Repo.clone_from('https://github.com/username/repo.git', 'repo')
    
    # Add the file to the repository
    repo.index.add(['data.csv'])
    
    # Commit the changes
    repo.index.commit('Add data.csv')
    
    # Push the changes to GitHub
    origin = repo.remote(name='origin')
    origin.push()
    
    # Show a success message
    st.success('Data saved to GitHub!')

# Add a button to trigger the save function
if st.button('Save data'):
    save_csv()