import streamlit as st
import pandas as pd

df = pd.read_csv('myfile.csv')

st.title('Chart elements')
st.sidebar.markdown('Yes, it is. chart elements! :sunglasses:')

st.area_chart(df)

st.bar_chart(df)

st.line_chart(df)

st.scatter_chart(df)