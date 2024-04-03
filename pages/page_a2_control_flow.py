import streamlit as st

# Forms
# Create a form that batches elements together with a "Submit" button.
with st.form(key='my_form'):
    name = st.text_input('Name')
    email = st.text_input('Email')
    st.form_submit_button('Sign up')

# Rerun script
# Rerun the script immediately.
# st.rerun()

# Stop execution
# Stop execution immediately.
# st.stop()

# Switch page
# Programmatically navigates to a specified page.
st.switch_page('pages/page1.py')