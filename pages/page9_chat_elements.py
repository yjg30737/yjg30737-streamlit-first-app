import streamlit as st
import numpy as np
from script import get_response

# Chat input
# Display a chat input widget.
prompt = st.chat_input('Say something')
if prompt:
    st.write(f'This user has sent: {prompt}')

# Chat message
# Insert a chat message container.
with st.chat_message('user'):
    st.write('Hello! :wave:')
    st.line_chart(np.random.randn(10, 2))

# Status container
# Display output of long-running tasks in a container.

st.write_stream(get_response('What is the music of life?'))

import time

def do_something_slow():
    time.sleep(10)
    st.write('Done!')

with st.status('Running'):
    do_something_slow()
