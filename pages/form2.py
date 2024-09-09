import streamlit as st

with st.form("vehicle_condition_form"):
    st.subheader(
        f"""Are all of the wheels and tires inflated and on your {st.session_state['vehicle_make']}?"""
    )
    st.markdown(
        "No biggie either way, we're just trying to select the best truck to pick 'er up."
    )
    tires_status = st.radio(horizontal=True,
        label="Are the tires inflated?",
        options=["Yes", "No"],
        key="tires"
    )

# Column 2: Exterior Glass/Mirror damage
    st.subheader(f"""Are any mirrors, glass, or lights damaged or missing?""")
    exterior_damage_status = st.radio(horizontal=True,
        label="Exterior Damage?",
        options=["No Damage", "Yes, at least one or more parts are damaged"],
        key="exterior_glass_damage"
    )
    
    _,col1,_ = st.columns([1,2,1])
    with col1:
        final_submit = st.form_submit_button("Next", use_container_width=True, type='primary')

    if final_submit:
        st.switch_page("pages/form_condition.py")

_,col1,_ = st.columns([1,2,1])
with col1:
    if st.button("Previous", use_container_width=True, type='secondary'):
        st.switch_page("pages/form.py")