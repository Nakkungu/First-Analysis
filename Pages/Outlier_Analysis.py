import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Load data
df = pd.read_excel('Assessedsites_Fully_Assessed_Woredas_Trail_Bridges_Only_TableToExcel.xlsx')

Q1 = df[['NEAR_DIST', 'metric', 'POPULATION']].quantile(0.25)
Q3 = df[['NEAR_DIST', 'metric', 'POPULATION']].quantile(0.75)
IQR = Q3 - Q1

# Define upper and lower bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers for each variable
outliers_near_dist = df[(df['NEAR_DIST'] < lower_bound['NEAR_DIST']) | (df['NEAR_DIST'] > upper_bound['NEAR_DIST'])]
outliers_metric = df[(df['metric'] < lower_bound['metric']) | (df['metric'] > upper_bound['metric'])]
outliers_population = df[(df['POPULATION'] < lower_bound['POPULATION']) | (df['POPULATION'] > upper_bound['POPULATION'])]

#import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Create the scatter plot with outliers
fig_map_outliers_names = go.Figure()

# Add scatter plot traces for data points and outliers
fig_map_outliers_names.add_trace(go.Scatter(
    x=df['GPS__Longi'],
    y=df['GPS__Latit'],
    mode='markers',
    marker=dict(color='blue'),
    name='Data Points',
    text=df['Opportunit'],  # Use the 'Name' column for text annotations
    hoverinfo='text'  # Show text on hover
))

fig_map_outliers_names.add_trace(go.Scatter(
    x=outliers_near_dist['GPS__Longi'],
    y=outliers_near_dist['GPS__Latit'],
    mode='markers',
    marker=dict(color='red'),
    name='Outliers (NEAR_DIST)',
    text=outliers_near_dist['Opportunit'],  # Use the 'Name' column for text annotations
    hoverinfo='text'  # Show text on hover
))

fig_map_outliers_names.add_trace(go.Scatter(
    x=outliers_metric['GPS__Longi'],
    y=outliers_metric['GPS__Latit'],
    mode='markers',
    marker=dict(color='green'),
    name='Outliers (metric)',
    text=outliers_metric['Opportunit'],  # Use the 'Name' column for text annotations
    hoverinfo='text'  # Show text on hover
))

fig_map_outliers_names.add_trace(go.Scatter(
    x=outliers_population['GPS__Longi'],
    y=outliers_population['GPS__Latit'],
    mode='markers',
    marker=dict(color='orange'),
    name='Outliers (POPULATION)',
    text=outliers_population['Opportunit'],  # Use the 'Name' column for text annotations
    hoverinfo='text'  # Show text on hover
))

# Layout for scatter plot
fig_map_outliers_names.update_layout(
    title='Locations of Outliers with Names',
    xaxis_title='Longitude',
    yaxis_title='Latitude'
)

# Concatenate outliers from different variables into one DataFrame
outlier_table = pd.concat([outliers_near_dist, outliers_metric, outliers_population])

# Add the 'Woreda' column from the original DataFrame 'df' to the outlier table
outlier_table['Woreda'] = df.loc[outlier_table.index, 'Woreda']

# Create a table trace
table_trace = go.Table(
    header=dict(values=['Woreda', 'Opportunit', 'NEAR_DIST', 'metric', 'POPULATION'],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[outlier_table['Woreda'], outlier_table['Opportunit'], outlier_table['NEAR_DIST'], outlier_table['metric'], outlier_table['POPULATION']],
               fill=dict(color=[outlier_table['metric'].apply(lambda x: 'green' if x in outliers_metric['metric'].values else 'orange' if x in outliers_population['metric'].values else 'red')]),
               align='left')
)

# Layout for the table
table_layout = go.Layout(
    title='Outlier Data Table'
)

# Add the table trace to the figure
fig_with_table = go.Figure(data=[table_trace], layout=table_layout)

# Display the table in Streamlit
st.plotly_chart(fig_map_outliers_names)
st.plotly_chart(fig_with_table)
