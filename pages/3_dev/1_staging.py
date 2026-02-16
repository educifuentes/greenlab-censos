import streamlit as st

from models.staging._stg_censo_2024__personas import get_stg_censo_2024__personas

from utilities.ui_components.render_model import render_model_ui
from utilities.ui_components.icons import render_icon

# Page settings and header
st.title("Staging")

# Create tabs for organization
tab1, tab2 = st.tabs([
    f"{render_icon('person')} personas",
    f"{render_icon('hogares')} hogares",
])

with tab1:
    censo_2024__personas_df = get_stg_censo_2024__personas()
    render_model_ui(censo_2024__personas_df, table_name="Personas")

with tab2:
    st.header("Hogares")
    st.info("Capa hogares en desarrollo")