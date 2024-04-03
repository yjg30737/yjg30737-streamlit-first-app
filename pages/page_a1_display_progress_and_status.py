import time

import streamlit as st

def show_basic_progress_bar(n1, n2):
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(n1, n2 + 1):
        progress_bar.progress(i)
        status_text.text(f"{i}%")
        time.sleep(0.05)
    progress_bar.empty()
    status_text.empty()

# Progress bar
# Display a progress bar.
show_basic_progress_bar(0, 100)

# Spinner
# Temporarily displays a message while executing a block of code.
with st.spinner('Please wait...'):
    time.sleep(5)

# Status container
# Display output of long-running tasks in a container.
with st.status('Running'):
    time.sleep(5)

# Toast
# Briefly displays a toast message in the bottom-right corner.
st.toast('Butter!', icon='🦄')

# Balloons
# Display celebratory balloons!
st.balloons()

# Snowflakes
# Display celebratory snowflakes!
st.snow()

# Error box
# Display error message.
st.error('This is an error message')

# Warning box
# Display warning message.
st.warning('This is a warning message')

# Info box
# Display info message.
st.info('This is an info message')

# Success box
# Display success message.
st.success('This is a success message')

# Exception
# Display exception message.
try:
    raise RuntimeError('This is an exception')
except RuntimeError as e:
    st.exception(e)