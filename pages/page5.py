import streamlit as st
import pandas as pd

filename = 'myfile.csv'

df = pd.read_csv(filename)

clicked = st.button('Click me!')

edited = st.data_editor(df, num_rows='dynamic')

f = open(filename, 'r')

st.download_button('Download', f, file_name=filename)

st.link_button('Link', url='https://www.streamlit.io/')

for i in range(5):
    selected = st.checkbox(f'Checkbox {i}')

activated = st.toggle('Activate')

choice = st.radio('Radio', ['A', 'B', 'C'])

selectbox_choice = st.selectbox('Select', ['A', 'B', 'C'])

choices = st.multiselect('Multiselect', ['A', 'B', 'C'])

number = st.slider('Slider', min_value=0, max_value=100)

size = st.select_slider('Pick a size', options=['S', 'M', 'L'])

name = st.text_input('First name')

choice = st.number_input('Pick a number', 0, 10)

text = st.text_area('Text to translate')

date = st.date_input('Your birthday')

time = st.time_input('Meeting time')

data = st.file_uploader('Upload a CSV', type='csv')

image = st.camera_input('Take a picture')

color = st.color_picker('Pick a color')