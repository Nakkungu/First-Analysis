import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title='Histograms',
    page_icon='📜',
    layout='wide'
)

import streamlit as st
import plotly.graph_objects as go

df = pd.read_excel('Assessedsites_Fully_Assessed_Woredas_Trail_Bridges_Only_TableToExcel.xlsx')

# Histogram for NEAR_DIST
fig1 = go.Figure(go.Histogram(
    x=df['NEAR_DIST'],
    nbinsx=100,  # Adjust the number of bins as needed
    marker_color='blue',  # Use marker_color for bar area color
    opacity=0.7,
    name='NEAR_DIST'
))
fig1.update_layout(
    title='Distribution of NEAR_DIST',
    xaxis_title='NEAR_DIST',
    yaxis_title='Frequency'
)

# Histogram for metric
fig2 = go.Figure(go.Histogram(
    x=df['metric'],
    nbinsx=100,  # Adjust the number of bins as needed
    marker_color='green',
    opacity=0.7,
    name='metric'
))
fig2.update_layout(
    title='Distribution of metric',
    xaxis_title='metric',
    yaxis_title='Frequency'
)

# Histogram for POPULATION
fig3 = go.Figure(go.Histogram(
    x=df['POPULATION'],
    nbinsx=100,  # Adjust the number of bins as needed
    marker_color='orange',
    opacity=0.7,
    name='POPULATION'
))
fig3.update_layout(
    title='Distribution of POPULATION',
    xaxis_title='POPULATION',
    yaxis_title='Frequency'
)

# Display plots in Streamlit
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)



# Plot histogram for 'Woreda' column
fig = px.histogram(df, x='Woreda', title='Histogram of Woreda')

# Display the plot using Streamlit
st.plotly_chart(fig)

