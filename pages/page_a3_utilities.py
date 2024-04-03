import pandas as pd
import streamlit as st

# Set page title, favicon, and more
# Configures the default settings of the page.
st.set_page_config(
    page_title='My App',
    page_icon='🧊',
)

# Echo
# Display some code on the app, execute it.
# Useful for tutorials.
with st.echo():
    st.write('This code will be printed')

# Get help
# Display object's doc string, nicely formatted.
arr = [st.write, print]

for obj in arr:
    st.help(obj)

# Query parameters
# Get, set, or clear the query parameters that are shown in the browser's URL bar.
obj = { 'key': 'value' }
for key, value in obj.items():
    st.query_params[key] = value
    # st.query_params.clear()