import streamlit as st

# Initialize session state for dark mode if not set
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = True  # Default to dark mode

# Sidebar Navigation
st.sidebar.title("Unit Converter")
st.sidebar.subheader("Choose Conversion Type")
conversion_type = st.sidebar.selectbox("Select Type", ["Length", "Weight", "Temperature"])

# Dark Mode Toggle
dark_mode_toggle = st.sidebar.checkbox("☀️ Light Mode", value=not st.session_state.dark_mode)
if dark_mode_toggle:
    st.session_state.dark_mode = False
    st.markdown("""
        <style>
            body {
                background-color: white;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.session_state.dark_mode = True
    st.markdown("""
        <style>
            body {
                background-color: #1e1e1e;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# Conversion Logic
def convert_length(value, from_unit, to_unit):
    length_units = {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371, "Foot": 3.28084, "Inch": 39.3701}
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value

# Input Fields
st.title("Unit Converter")
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if conversion_type == "Length":
    from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Mile", "Foot", "Inch"])
    to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Mile", "Foot", "Inch"])
    result = convert_length(value, from_unit, to_unit)
elif conversion_type == "Weight":
    from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Pound", "Ounce"])
    to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Pound", "Ounce"])
    result = convert_weight(value, from_unit, to_unit)
elif conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)

if st.button("Convert"): 
    st.success(f"Converted Value: {result:.2f} {to_unit}")
