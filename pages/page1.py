import streamlit as st
from openai import OpenAI
from script import get_response

from settings import OPENAI_API_KEY

st.title('Display almost anything! :sunglasses:')
st.sidebar.markdown('To good to be true! :sunglasses:')

st.subheader('Write')
st.write('Hello, *World!* :sunglasses:')

st.subheader('Write - Stream')

response = get_response('What sense does that make?')

st.write_stream(response)

st.subheader('Write - Magic')
'Hello **world** :sunglasses:'

