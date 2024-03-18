import streamlit as st
from openai import OpenAI

from settings import OPENAI_API_KEY

st.title('Display almost anything! :sunglasses:')
st.sidebar.markdown('To good to be true! :sunglasses:')

st.subheader('Write')
st.write('Hello, *World!* :sunglasses:')

st.subheader('Write - Stream')
openai_client = OpenAI(api_key=OPENAI_API_KEY)

openai_arg = {
    "model": 'gpt-3.5-turbo',
    "messages": [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'What is the purpose of life? Make it very short!'}],
    "n": 1,
    "stream": True,
}
response = openai_client.chat.completions.create(**openai_arg)

st.write_stream(response)

st.subheader('Write - Magic')
'Hello **world** :sunglasses:'

