from os.path import split

import streamlit as st
import pandas as pd
import plotly.express as px

st.title('In Search for Happiness')

df = pd.read_csv('happy/happy.csv')

data = ['GDP', 'Happiness', 'Generosity']


x_axis = st.selectbox('Select the data for the X-axis', data)
y_axis = st.selectbox('Select the data for the Y-axis', data)
match x_axis:
    case 'GDP':
        x_array = df['gdp']
    case 'Happiness':
        x_array = df['happiness']
    case 'Generosity':
        x_array = df['generosity']

match y_axis:
    case 'GDP':
        y_array = df['gdp']
    case 'Happiness':
        y_array = df['happiness']
    case 'Generosity':
        y_array = df['generosity']

st.subheader(f'{x_axis} and {y_axis}')

figure = px.scatter(x=x_array, y=y_array, labels={'x': x_axis, 'y':y_axis})

st.plotly_chart(figure)





