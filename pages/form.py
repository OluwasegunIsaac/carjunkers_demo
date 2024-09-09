import streamlit as st

# Initialize session state variables
if "vehicle_make" not in st.session_state:
    st.session_state["vehicle_make"] = "Vehicle"  # Placeholder value

if "show_next_questions" not in st.session_state:
    st.session_state["show_next_questions"] = False  

# Create a form for vehicle condition
with st.form("vehicle_condition_form"):
    st.subheader(f"Tell us more about your {st.session_state['vehicle_make']}")

    st.markdown(
        f"""Is the {st.session_state['vehicle_make']}'s battery working and do you have a working key or fob?"""
    )
    st.markdown(
        f"""We need to know if your car will start. Having the key or a working fob and a 
        properly installed, working battery (without needing to be jumped) will get you a higher offer."""
    )
    battery_status = st.radio(horizontal=True,
        label="Is the battery working?",
        options=["Yes", "No"],
        key="battery"
    )

# Column 2: Car Start / Drivability status
    st.subheader(f"""Can you start and drive your {st.session_state['vehicle_make']}?""")
    st.markdown(
        f"""This tells us about your {st.session_state['vehicle_make']}'s condition and also helps us figure out the best tow truck to use for pickup."""
    )
    drivable_status = st.radio(horizontal=True,
        label="Can the car be driven?",
        options=["Yes", "No"],
        key="drivable"
    )
    _,col1,_ = st.columns([1,2,1])
    with col1:
        final_submit = st.form_submit_button("Next", use_container_width=True, type='primary') 

    if final_submit:
        st.switch_page("pages/form2.py")

_,col1,_ = st.columns([1,2,1])
with col1:
    if st.button("Go to homepage", use_container_width=True, type='secondary'):
        st.switch_page("pages/landing_page.py")