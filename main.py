import streamlit as st

st.set_page_config(layout="wide")

# Hiding the sidebar using custom CSS
hide_sidebar_style = """
    <style>
    /* Hide the Streamlit sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# --- PAGE SETUP ---
home = st.Page(page="pages/landing_page.py", title="Home", icon=":material/home:", default=True)
form = st.Page(page="pages/form.py", title="Stage 1", icon=":material/bar_chart:")
form2 = st.Page(page="pages/form2.py", title="Stage 1b", icon=":material/bar_chart:")
form_condition = st.Page(page="pages/form_condition.py", title="Stage 2", icon=":material/analytics:")
form_condition2 = st.Page(page="pages/form_condition2.py", title="Stage 2", icon=":material/analytics:")
form_ownership = st.Page(page="pages/form_ownership.py", title="Stage 3", icon=":material/data_table:")
generate_offer = st.Page(page="pages/generate_offer.py", title="Offer", icon=":material/data_table:")

# --- NAVIGATION SETUP ---
pg = st.navigation(pages=[home, form, form2, form_condition, form_condition2, form_ownership, generate_offer])

# --- COMMON TO ALL PAGES ---
# st.logo("assets/xxx.png")

pg.run()
