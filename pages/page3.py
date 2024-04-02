import folium
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from streamlit_folium import st_folium
from streamlit_image_coordinates import streamlit_image_coordinates

st.title('Data elements')
st.sidebar.markdown('Yes, it is. data elements! :sunglasses:')

df = pd.read_csv('test_csv.csv')

st.header('Dataframes')
st.subheader('Display a dataframe as an interactive table.')
st.dataframe(df)

st.header('Data editor')
st.subheader('Display a data editor widget.')
edited = st.data_editor(df, num_rows='dynamic')

st.header('Column configuration')
st.subheader('Configure the display and editing behavior of dataframes and data editors.')

st.column_config.NumberColumn('Price (in USD)', min_value=0, format='$%d')

st.header('Static tables')
st.subheader('Display a static table.')
st.table(df)

st.header('Metrics')
st.subheader('Display a metric in big bold font, with an optional indicator of how the metric changed.')
st.metric('My metric', 42, 2)

# Make sample dictionary
my_dict = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [23, 36, 43, 28],
    'city': ['New York', 'Paris', 'Berlin', 'London']
}

st.header('Dicts and JSON')
st.subheader('Display object or string as a pretty-printed JSON string.')
st.json(my_dict)

df = pd.read_csv('myfile.csv')

st.header('Streamlit Folium')

m = folium.Map(location=[45.5236, -122.6750])
folium.Marker([45.5236, -122.6750], popup='Portland, OR').add_to(m)
st_data = st_folium(m)

st.header('Streamlit Image Coordinates')

value = streamlit_image_coordinates("sample.png")
st.write(value)

st.header('Streamlit Plotly Events')

st.header('Streamlit Ag-Grid')
AgGrid(df)