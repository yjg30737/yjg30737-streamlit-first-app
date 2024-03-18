import streamlit as st

st.title('Text elements')
st.sidebar.markdown('Yes, it is. text elements! :sunglasses:')
st.sidebar.divider()

st.header('This is a header!')

st.subheader('This is a subheader!')

st.caption('This is written in a caption!')

st.code('print("Hello, World!")')

st.text('This is a simple text!')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.divider()

st.subheader('Isn\'t it amazing? :sunglasses:')

st.header('Third party components')

from streamlit_tags import st_tags
from annotated_text import annotated_text

keywords = st_tags(
    label='Enter a keyword:',
    text='Press enter to add more',
    value=['Python', 'Data Science'],
    suggestions=['Data', 'Science', 'Python', 'Pandas', 'Plotly']
)

annotated_text(
    ('This will', 'red'),
    (' be ', 'green'),
    ('annotated', '#8ef')
)

import pandas as pd
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
if canvas_result.json_data is not None:
    objects = pd.json_normalize(canvas_result.json_data["objects"])  # need to convert obj to str because PyArrow
    for col in objects.select_dtypes(include=['object']).columns:
        objects[col] = objects[col].astype("str")
    st.dataframe(objects)