import streamlit as st
from queryfile import query_
from createdatabase import update_database

import sys
import os
file_directory = os.path.join(os.path.dirname(__file__), 'data')
sys.path.append(file_directory)


from updatefile import update





# Define the function to be invoked when the button is clicked
def my_function():
    st.write("Button clicked!")

# Create a container for the button
with st.container():
    # Create a small button in the top left corner
    if st.button("update database", key="small_button"):
        update()
        update_database()


# Main content of your Streamlit app
st.title("Tech News Query Bot")
query = st.text_input("Enter your question:")

if st.button("Submit"):
    if query:
        Response = query_(query)
        st.write(Response)
    else:
        st.write("Please enter a query.")
