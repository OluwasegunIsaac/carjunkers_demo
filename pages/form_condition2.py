import streamlit as st

# Initialize session state variables
if "vehicle_make" not in st.session_state:
    st.session_state["vehicle_make"] = "Vehicle"  # Placeholder value
if "show_next_questions" not in st.session_state:
    st.session_state["show_next_questions"] = False  # Tracks whether to show the next set of questions

vehicle_make = st.session_state["vehicle_make"]

with st.form(key="additional_info_form"):
    
    # Catalytic converter
    st.subheader(f"Does your {vehicle_make} have its catalytic converter?")
    st.markdown(
        """You'll know it's missing if your car makes a loud roar when you start it and gets louder as you 
        accelerate. You might also notice an increase in exhaust fumes. Finally, you can check for missing 
        parts under the car, around the muffler."""
    )
    catalytic_converter = st.radio(horizontal=True,
        key="catalytic_converter",
        label="Catalytic Converter",
        label_visibility="hidden",
        options=["Yes, it's attached", "No, it's missing"],
    )


    # Interior missing parts or damaged?
    st.subheader(f"Does the interior of your {vehicle_make} have missing parts or major damage?")
    st.markdown(
        """Think about the seats, airbags, and dashboard. Don't worry about small scratches or spots. 
        We just need to know if there are any serious rips or tears."""
    )
    interior_damage = st.radio(horizontal=True,
        key="interior_damage",
        label="Interior Damage",
        label_visibility="hidden",
        options=["No, All interior parts are in good condition", "Yes, some interior damage"],
    )

    _,col1,_ = st.columns([1,2,1])
    with col1:
        final_submit = st.form_submit_button("Next", use_container_width=True, type='primary')

    if final_submit:
        st.switch_page("pages/form_ownership.py")

_,col1,_ = st.columns([1,2,1])
with col1:
    if st.button("Previous", use_container_width=True, type='secondary'):
        st.switch_page("pages/form_condition.py")
