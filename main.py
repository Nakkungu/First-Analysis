<<<<<<< HEAD
import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title='Login',
    page_icon='🪵',
    layout='wide'
)

=======
import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title='Login',
    page_icon='🪵',
    layout='wide'
)

with st.expander("Columns of Interest Descriptions", expanded=True):
            st.info("""
            - **NEAR_DIST**: Distance between the assessed site in the database and the nearest remotely identified site
            - **metric**: Measure of impact for remotely identified site
            - **Population**: Population count in !km radius of assessed site
            - **GPS_Latit**: GPS latitude for assessed site
            - **GPS_Longi**: GPS longitude for assessed site
                    """)
>>>>>>> a16ff69eb4bf00c4cec6e82e5833cb2de4639149
