import streamlit as st

# State management
st.title('State management')
# Session state
# Session state is a way to share variables between rerus, for each user session.

st.session_state['key'] = '245'
# st.rerun()
st.write(st.session_state['key'])