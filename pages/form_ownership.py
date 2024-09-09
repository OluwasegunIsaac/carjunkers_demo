import streamlit as st

# Initialize session state variables
if "vehicle_make" not in st.session_state:
    st.session_state["vehicle_make"] = "Vehicle"  # Placeholder value
if "show_next_questions" not in st.session_state:
    st.session_state["show_next_questions"] = False  # Tracks whether to show the next set of questions

# Create a form for vehicle ownership details
with st.form("vehicle_ownership_form"):
    st.header(f"Tell us more about your {st.session_state['vehicle_make']}")

    #Ownership

    st.subheader(f"""Do you own the {st.session_state['vehicle_make']}?""")
    st.markdown(
        '''Let us know if you fully own it, are making payments, or it's a leased vehicle.'''
    )
    ownership_status = st.radio(horizontal=True,
        label="Ownership Status",
        options=[
            "Yes, I own it completely",
            "No, I'm still making payments",
            "No, I make lease payments"
        ],
        key="ownership"
    )

    #Clean title status
    st.subheader(f"Does your {st.session_state['vehicle_make']} have a clean title?")
    st.markdown(
        '''Most cars without severe damage have a clean title. Check for a note or stamp that says 'salvage' or 'rebuilt'.'''
    )
    clean_title_status = st.radio(horizontal=True,
        label="Clean Title?",
        options=["Yes, Clean Title", "No, Salvage Title", "I don't have the title"],
        key="clean_title"
    )

    #3
    st.subheader(f"Has your {st.session_state['vehicle_make']} ever been in a flood or fire?")
    st.markdown(
        '''It's unfortunate, but it happens. Let us know if your car has been in a fire or flood incident.'''
    )
    flood_fire_status = st.radio(horizontal=True,
        label="Flood or Fire Damage?",
        options=["No, Thank Goodness", "Yes, it has been in a flood or fire"],
        key="flood_fire_damage"
    )

    _,col1,_ = st.columns([1,2,1])
    with col1:
        final_submit = st.form_submit_button("Next", use_container_width=True, type='primary')

    if final_submit:
        st.switch_page("pages/generate_offer.py")

_,col1,_ = st.columns([1,2,1])
with col1:
    if st.button("Previous", use_container_width=True, type='secondary'):
        st.switch_page("pages/form_condition2.py")

