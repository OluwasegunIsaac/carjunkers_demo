import streamlit as st

# Initialize session state variables
if "vehicle_make" not in st.session_state:
    st.session_state["vehicle_make"] = "Vehicle"  # Placeholder value
if "show_next_questions" not in st.session_state:
    st.session_state["show_next_questions"] = False  # Tracks whether to show the next set of questions

vehicle_make = st.session_state["vehicle_make"]

# First Form for Exterior Questions
with st.form(key="exterior_form"):

    # Condition - Exterior Damage
    st.subheader(f"Does your {vehicle_make} have exterior damage?")
    st.markdown(
        """Most used cars have a little wear and tear, but small blemishes won't affect your offer. 
        Just let us know if the outside of your car has any damage bigger than a baseball."""
    )
    exterior_damage = st.radio(horizontal=True,
        key="exterior_damage",
        label="Exterior Damage",
        label_visibility="hidden",
        options=["Nothing Major", "Yes, some rust or exterior damage"]
    )

    # Doors / Bumpers / Exterior Parts
    st.subheader(f"Are the doors, bumpers, and other exterior parts and panels attached?")
    st.markdown(
        """We're talking just as secure as when it left the factory, or a sturdy aftermarket replacement. 
        Nothing loose, hanging or missing."""
    )
    exterior_parts_attached = st.radio(horizontal=True,
        key="exterior_parts_attached",
        label="Exterior Parts",
        label_visibility="hidden",
        options=[
            "Yes, all exterior parts are attached",
            "No, at least one or more parts are not attached",
        ],
    )

    _,col1,_ = st.columns([1,2,1])
    with col1:
        final_submit = st.form_submit_button("Next", use_container_width=True, type='primary')

    if final_submit:
        st.switch_page("pages/form_condition2.py")

_,col1,_ = st.columns([1,2,1])
with col1:
    if st.button("Previous", use_container_width=True, type='secondary'):
        st.switch_page("pages/form2.py")
