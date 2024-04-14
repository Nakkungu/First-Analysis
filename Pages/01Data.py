import streamlit as st

import pandas as pd

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title='Data',
    page_icon='📜',
    layout='wide'
)

import pandas as pd
import streamlit as st

def select_all_features():
    df = pd.read_excel('Assessedsites_Fully_Assessed_Woredas_Trail_Bridges_Only_TableToExcel.xlsx')
    return df

if __name__ == "__main__":
    # Read all features
    all_data = select_all_features()

    # Sidebar to select option
    option = st.sidebar.selectbox("Select data type", ["All Data", "Columns of Interest"])

    # Display corresponding data
    if option == "All Data":
        st.title("All Data")
        st.write(all_data)
    elif option == "Columns of Interest":
        # Select only the columns of interest
        columns_of_interest = ['NEAR_DIST', 'metric', 'POPULATION', 'GPS__Latit', 'GPS__Longi', 'Woreda', 'Opportunit']
        df_columns_of_interest = all_data[columns_of_interest]

        # Display the table with columns of interest
        st.title("Columns of Interest")
        st.write(df_columns_of_interest)

        # Display expander for column descriptions
        with st.expander("Columns of Interest Descriptions", expanded=True):
            st.info("""
            - **NEAR_DIST**: Distance between the assessed site in the database and the nearest remotely identified site
            - **metric**: Measure of impact for remotely identified site
            - **POPULATION**: Population count in !km radius of assessed site
            - **GPS_Latit**: GPS latitude for assessed site
            - **GPS_Longi**: GPS longitude for assessed site
            - **Woreda**: Second last administrative division in Ethiopia
            - **Opportunit**: Assessed site name 
            """)

