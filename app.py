import streamlit as st
from utilities.ui_components.icons import ICONS

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Greenlab Censos | Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- PAGE SETUP ---
# Defining the pages based on the directory structure
pages = {
    "Vistas": [
        st.Page("pages/1_views/1_overview.py", title="Overview", icon=":material/dashboard:"),
    ],
    "Herramientas": [
        st.Page("pages/2_tools/1_documentation.py", title="Documentación", icon=ICONS["documentation"]),
        st.Page("pages/2_tools/2_validations.py", title="Validaciones de Datos", icon=ICONS["check"]),
        st.Page("pages/2_tools/3_explorer.py", title="Explorador de Datos", icon=":material/search:"),
    ],
    "Desarrollo": [
        st.Page("pages/3_dev/1_staging.py", title="Capa Staging", icon=":material/layers_clear:"),
        st.Page("pages/3_dev/2_intermediate.py", title="Capa Intermedia", icon=":material/settings_input_component:"),
        st.Page("pages/3_dev/3_marts.py", title="Capa Marts", icon=":material/database:"),
        st.Page("pages/3_dev/4_bi_tables.py", title="Tablas BI", icon=ICONS["metrics"]),
    ],
}

# --- NAVIGATION ---
pg = st.navigation(pages)

# --- SIDEBAR & BRANDING ---
with st.sidebar:
    st.markdown("# 🌿 Greenlab")
    st.markdown("---")

# --- RUN NAVIGATION ---
pg.run()