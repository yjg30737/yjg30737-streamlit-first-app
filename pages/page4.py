import streamlit as st
import pandas as pd
import pydeck as pdk

df = pd.read_csv('myfile.csv')

st.title('Chart elements')
st.sidebar.markdown('Yes, it is. chart elements! :sunglasses:')

st.area_chart(df)

st.bar_chart(df)

st.line_chart(df)

st.scatter_chart(df)

# For map
# st.map(df)

# For none-ambiguous data
# st.pyplot(df)

# Altair chart (if you're interested)
# st.altair_chart(df)

# Vega-Lite chart (if you're interested)
# st.vega_lite_chart(df)

# Display an interactive plotly chart
# The `figure_or_data` positional argument
# must be `dict`-like, `list`-like,
# or an instance of plotly.graph_objs.Figure
# st.plotly_chart(df)

# Display an interactive bokeh chart
# st.bokeh_chart(df)

st.page_link('pages/2_🌍_Mapping_Demo.py', icon='🌍', label='Mapping Demo')