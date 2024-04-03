import streamlit as st
import pandas as pd

st.title('Mutate Charts')

df = pd.read_csv('myfile.csv')

# Add rows
# Append a dataframe to the bottom of the current one in certain elements, for optimized data updates.
df_key = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

df_with_extra_rows = pd.DataFrame([
    [6, 148, 72, 35, 0, 33.6, 0.627, 50, 1],
    [1, 85, 66, 29, 0, 26.6, 0.351, 31, 0],
    [8, 183, 64, 0, 0, 23.3, 0.672, 32, 1]
], columns=df_key)

element = st.line_chart(df)
element.add_rows(df_with_extra_rows)
