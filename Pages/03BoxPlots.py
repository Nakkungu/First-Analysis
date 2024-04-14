import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.switch_page_button import switch_page
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(
    page_title='BoxPlots',
    page_icon='📜',
    layout='wide'
)


# Read the Excel file into a DataFrame
df = pd.read_excel('Assessedsites_Fully_Assessed_Woredas_Trail_Bridges_Only_TableToExcel.xlsx')

# Create subplots with larger size and separated horizontally
fig = make_subplots(rows=1, cols=3, subplot_titles=('NEAR_DIST', 'metric', 'POPULATION'), horizontal_spacing=0.15)

# Add box plots for NEAR_DIST
fig.add_trace(go.Box(y=df['NEAR_DIST'], name='NEAR_DIST', marker_color='blue'), row=1, col=1)

# Add box plots for metric
fig.add_trace(go.Box(y=df['metric'], name='metric', marker_color='green'), row=1, col=2)

# Add box plots for POPULATION
fig.add_trace(go.Box(y=df['POPULATION'], name='POPULATION', marker_color='orange'), row=1, col=3)

# Update layout to increase the size of the figure
fig.update_layout(
    title='Box Plot of Numeric Variables',
    yaxis_title='Value',
    height=400,  # Adjust the height of the figure
    width=1000,  # Adjust the width of the figure
)

# Display the plot using Streamlit
st.plotly_chart(fig)

