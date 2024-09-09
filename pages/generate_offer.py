import streamlit as st

# Initialize session state variables if they do not exist
if "vehicle_year" not in st.session_state:
    st.session_state["vehicle_year"] = "2020"  # Default or placeholder value
if "vehicle_make" not in st.session_state:
    st.session_state["vehicle_make"] = "Vehicle Make"  # Default or placeholder value
if "vehicle_model" not in st.session_state:
    st.session_state["vehicle_model"] = "Vehicle Model"  # Default or placeholder value
if "offer_amount" not in st.session_state:
    st.session_state["offer_amount"] = 0  # Default or placeholder value

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

# Generate the offer
offer_id, st.session_state["offer_amount"] = offerService.generate_offer()

vehicle_year = st.session_state["vehicle_year"]
vehicle_model = st.session_state["vehicle_model"]
vehicle_make = st.session_state["vehicle_make"]
offer_amount = st.session_state["offer_amount"]

con = st.container(border=True)
col1, col2,_ = con.columns([4,2,1])
with col1:
    st.markdown("""
    <style>
    .spacing {
        margin-top: -30px;
        margin-bottom: -70px; 
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<h2 class='spacing' style='text-align: left;'>Ta da!</h1>", unsafe_allow_html=True)
    st.subheader(f"""We'd love to buy your {vehicle_year} {vehicle_make} {vehicle_model} for:""")
with col2:
    st.metric(label="Offer Amount", value=f"${offer_amount}", help='Buying price for your vehicle')


c1, c2 = st.columns(2)
with c1:
    st.subheader(f"How did we reach {offer_amount}")
    st.markdown(
        "The three main criteria we use to calculate our offers are market value, vehicle condition, and documentation (like title status)."
    )
with c2:
    st.subheader(f"What happens next?")
    st.write(
        "If you haven't already created an account, you'll do that, and accept our offer (assuming you want to do that). Then, you'll let us know who to pay and when to pick that car up. Easy peasy!"
    )

lowercolumn1, lowercolumn2 = st.columns(2)
with lowercolumn1:
    with st.expander("How do we calculate offers?"):
        st.markdown(
            """
            Our offer is based on all the information you gave us, which we break down into three buckets.
            """
        )
        st.markdown("<h6 style='text-align: left;'>Market Value</h6>", unsafe_allow_html=True)
        st.markdown(
            "Based on where your car is, we determine what your car is worth in your local area."
        )
        st.markdown("<h6 style='text-align: left;'>Vehicle condition</h6>", unsafe_allow_html=True)
        st.markdown(
            "All those little details you shared about the shape of your car, inside and out."
        )
        st.markdown("<h6 style='text-align: left;'>Documentation</h6>", unsafe_allow_html=True)
        st.markdown(
            "Right now we can only make offers on a car you own outright, so if you are leasing or paying off a car loan, we can't buy it from you."
        )
with lowercolumn2:
    with st.expander("What Happens Next?"):
        st.markdown(
            """
            You're nearly done. Now just a few tiny steps and your car will be sold.
            """
        )
        st.markdown("<h6 style='text-align: left;'>Accept your Offer</h6>", unsafe_allow_html=True)
        st.markdown(
            "The process is pretty lickety-split, but we'll let you know what's what along the way."
        )
        st.markdown("<h6 style='text-align: left;'>Schedule your pickup</h6>", unsafe_allow_html=True)
        st.markdown(
            "We'll connect you with a driver and coordinate your free pickup for a time that works best for you—as early as today."
        )
        st.markdown("<h6 style='text-align: left;'>Get Paid!</h6>", unsafe_allow_html=True)
        st.markdown(
            "When we come to get your car, we'll give it a quick once-over and hand you payment on the spot."
        )
 
st.write("")
_,col1,_ = st.columns([1,2,1])
with col1:
    if st.button("Previous", use_container_width=True, type='secondary'):
        st.switch_page("pages/form_ownership.py")
    if st.button("Go to homepage", use_container_width=True, type='primary'):
        st.switch_page("pages/landing_page.py")