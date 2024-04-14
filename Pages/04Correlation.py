import streamlit as st
import plotly.figure_factory as ff
import pandas as pd

# Load data
df = pd.read_excel('Assessedsites_Fully_Assessed_Woredas_Trail_Bridges_Only_TableToExcel.xlsx')

# Calculate correlation matrix
correlation_matrix = df[['NEAR_DIST', 'metric', 'POPULATION']].corr()

# Create annotated heatmap
fig = ff.create_annotated_heatmap(
    z=correlation_matrix.values,
    x=list(correlation_matrix.columns),
    y=list(correlation_matrix.index),
    colorscale='RdBu',  # Using a valid colorscale name
    annotation_text=correlation_matrix.values.round(2),
    showscale=True
)

# Update layout
fig.update_layout(
    title='Correlation Matrix of NEAR_DIST, metric, and POPULATION',
    xaxis_title='Variables',
    yaxis_title='Variables'
)

# Display the heatmap using Streamlit
st.plotly_chart(fig)
