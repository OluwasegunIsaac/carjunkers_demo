import streamlit as st
import json
import time
from streamlit_option_menu import option_menu

# Initialize session state variables at the top
if "key" not in st.session_state:
    st.session_state["key"] = "value"
    st.session_state["vehicle_year"] = ""
    st.session_state["vehicle_make"] = ""
    st.session_state["vehicle_model"] = ""
    st.session_state["offer_amount"] = ""
    st.session_state["quote_clicked"] = False

# Load the vehicle data from the JSON file
with open("./models/carlist.json", "r") as file:
    vehicles_data = json.load(file)

# OfferService Class
class OfferService:
    def __init__(self):
        pass

    def generate_offer(self):
        offer_id = "ABCDE"
        price = 500
        return offer_id, price

    def get_offer_by_id(self, offer_id):
        offer_id = "ABCDE"
        price = 500
        return price, offer_id

offerService = OfferService()

# Helper function to get models by brand
def get_models_by_brand(brand_name):
    for item in vehicles_data:
        if item["brand"].lower() == brand_name.lower():
            return item["models"]


st.markdown("""
    <style>
    .app-spacing {
        margin-top: -30px; /* No margin above */
        margin-bottom: -70px; /* Adjust the margin to reduce spacing */
    }
    </style>
    """, unsafe_allow_html=True)

# Reduced spacing for the heading
app_name = """
    <div class='app-spacing' style="padding:4px">
    <h1 style='text-align: left; color: #001236; font-size: 40px;'>Motor Market</h1>
    </div>
    """

col1, _ = st.columns([1, 3])

with col1:
    st.image('assets/logo.png', use_column_width=True)
    st.markdown(app_name, unsafe_allow_html=True)

st.divider()

# # Form for vehicle details
def stage_1_basic():
    make_options = [item["brand"] for item in vehicles_data]
    model_options = [""]
    year_options = [""] + list(range(2024, 1949, -1))

    # Select Year
    st.session_state["vehicle_year"] = st.selectbox(label="Year", options=year_options, key='year')
    
    # Select Make
    st.session_state["vehicle_make"] = st.selectbox(
        label="Make",
        options=[""] + sorted(make_options),
        disabled=not st.session_state["vehicle_year"],  # Disable if no year is selected
    )
    
    # Select Model (based on selected make)
    if st.session_state["vehicle_make"]:
        model_options = get_models_by_brand(st.session_state["vehicle_make"])
    st.session_state["vehicle_model"] = st.selectbox(
        label="Model",
        options=sorted(model_options),
        disabled=not st.session_state["vehicle_make"],  # Disable if no make is selected
    )
    
    # Trim Selection (Disabled for now, but can be extended)
    st.selectbox(
        label="Trim", options=[], disabled=not st.session_state["vehicle_make"]
    )

    # Location and Mileage inputs
    col1, col2 = st.columns(2)
    with col1:
        st.session_state["location"] = st.text_input(
            label="Location", placeholder="Dallas, Tx", disabled=not st.session_state["vehicle_model"]  # Disable if no model is selected
        )
    with col2:
        st.session_state["mileage"] = st.text_input(label="Mileage")

# Body content with text and image
col1,_, col2= st.columns([4,1,4])
with col1:
    # Custom CSS to adjust spacing
    st.markdown("""
        <style>
        .reduced-spacing {
            margin-bottom: -70px; /* Reduced spacing below */
        }
        .combined-spacing {
            margin-top: -70px; /* No margin above */
            margin-bottom: -70px; /* Reduced spacing below */
        }
        .end-spacing {
            margin-bottom: -30px; /* Reduced spacing below */
        }
        </style>
        """, unsafe_allow_html=True)

    # Headings with reduced spacing
    st.markdown("<h1 class='combined-spacing' style='text-align: left; font-size: 83px;'>INSTANT</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='reduced-spacing' style='text-align: left; font-size: 83px;'>CASH</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='reduced-spacing' style='text-align: left; font-size: 83px;'>FOR</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='reduced-spacing' style='text-align: left; font-size: 83px;'>JUNK</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='end-spacing' style='text-align: left; font-size: 80px;'>CARS.</h1>", unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: justify;">
    Our process is simple and straightforward. Tell us a little about your vehicle by filling out our contact
    form. If you've lost the title, we can still proceed with the sale, provided you have proof of ownership.
    </div>
    """,
    unsafe_allow_html=True
    )

with col2:
    st.markdown("""
        <style>
        .form-spacing {
            margin-top: -45px; /* Reduced spacing below */
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='form-spacing' style='text-align: left; font-size: 30px;'>We'll Have A Quote For You In No Time!</h1>", unsafe_allow_html=True)
    stage_1_basic()

    # Check if the form is valid (all required fields are selected)
    is_form_valid = (
        st.session_state.get("vehicle_year") 
        and st.session_state.get("vehicle_make") 
        and st.session_state.get("vehicle_model")
    )

    if st.button("Get Instant Quote", type="primary", key="quote", disabled=not is_form_valid, use_container_width=True):
        st.switch_page("pages/form.py")

st.divider()
st.markdown("""
        <style>
        .steps-spacing {
            margin-top: -70px; /* No margin above */
        }
        .steps2-spacing {
            margin-top: -20px; /* No margin above */
            margin-bottom: 0px;
        }
        </style>
        """, unsafe_allow_html=True)

st.markdown("<h1 class='steps-spacing' style='text-align: center; font-size: 40px;'>HOW IT WORKS</h1>", unsafe_allow_html=True)
st.markdown("<h1 class='steps2-spacing' style='text-align: center; font-size: 25px;'>4 simple steps to sell your junk car for cash:</h1>", unsafe_allow_html=True)

# Define columns
# Create placeholders for columns
placeholder_col1, placeholder_col2, placeholder_col3, placeholder_col4 = st.columns(4)

# Define the content for each column
col1_content = """
    <div style='text-align: center;'>
        <h1 style='font-size: 30px;'>1. Get a guaranteed cash quote</h1>
        <p>Speak with our experts and get the best cash offer. We commit to what we agree on the phone - no hidden fees or changes.</p>
    </div>
"""

col2_content = """
    <div style='text-align: center;'>
        <h1 style='font-size: 30px;'>2. Schedule a Pickup Time</h1>
        <p>We offer flexible pickup times from same-day service to scheduled times that fit your schedule.</p>
    </div>
"""

col3_content = """
    <div style='text-align: center;'>
        <h1 style='font-size: 30px;'>3. Have Your Vehicle Picked Up</h1>
        <p>Our tow truck will arrive at the agreed time, towing is free, and you'll get cash on the spot.</p>
    </div>
"""

col4_content = """
    <div style='text-align: center;'>
        <h1 style='font-size: 30px;'>4. Relax and Enjoy Your Cash</h1>
        <p>We handle the title transfer and ensure the vehicle is recycled responsibly. Enjoy peace of mind with our licensed, insured, and bonded service.</p>
    </div>
"""

# Create a button to start the content reveal
with placeholder_col1:
    st.markdown(col1_content, unsafe_allow_html=True)
    time.sleep(1.2)  # Adjust the delay as needed

with placeholder_col2:
    st.markdown(col2_content, unsafe_allow_html=True)
    time.sleep(1.2)  # Adjust the delay as needed

with placeholder_col3:
    st.markdown(col3_content, unsafe_allow_html=True)
    time.sleep(1.2)  # Adjust the delay as needed

with placeholder_col4:
    st.markdown(col4_content, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.markdown(
    """
    <h3 style='text-align: center; font-size: 20px;'>For an even faster quote, you can call us at <strong>817-494-0913</strong>. 
    We offer cash for vehicles in any condition, running or not, with or without title!</h3>""", unsafe_allow_html=True)
