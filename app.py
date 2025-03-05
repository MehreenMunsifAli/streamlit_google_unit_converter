import streamlit as st
import pandas as pd

def convert_units(value, from_unit, to_unit, conversion_type, conversion_types):
    if conversion_type == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    
    if from_unit == to_unit:
        return value
    
    # Convert to base unit then to target unit
    units = conversion_types[conversion_type]
    return value * units[from_unit] / units[to_unit]

def main():
    st.set_page_config(page_title="Google-Style Unit Converter", layout="centered")
    
    # Custom CSS to make it look more like Google
    st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stApp {
            max-width: 600px;
            margin: 0 auto;
        }
        .converter-card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        .header {
            color: #202124;
            font-family: 'Google Sans', Arial, sans-serif;
            margin-bottom: 20px;
        }
        .result {
            font-size: 24px;
            color: #202124;
            font-family: 'Google Sans', Arial, sans-serif;
            margin-top: 24px;
            margin-bottom: 10px;
            text-align: center;
            background-color:rgb(214, 232, 241);
            border-radius: 6px;
        }
        .unit-label {
            color: #5f6368;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Conversion categories and their units
    conversion_types = {
        "Length": {
            "Nanometer": 1e-9,
            "Micrometer": 1e-6,
            "Millimeter": 1e-3,
            "Centimeter": 1e-2,
            "Meter": 1,
            "Kilometer": 1e3,
            "Inch": 0.0254,
            "Foot": 0.3048,
            "Yard": 0.9144,
            "Mile": 1609.34,
            "Nautical mile": 1852
        },
        "Temperature": {
            "Celsius": "celsius",
            "Fahrenheit": "fahrenheit",
            "Kelvin": "kelvin"
        },
        "Weight": {
            "Microgram": 1e-9,
            "Milligram": 1e-6,
            "Gram": 1e-3,
            "Kilogram": 1,
            "Metric ton": 1000,
            "Ounce": 0.0283495,
            "Pound": 0.453592,
            "Stone": 6.35029,
            "Short ton": 907.185,
            "Long ton": 1016.05
        },
        "Volume": {
            "Milliliter": 1e-6,
            "Liter": 1e-3,
            "Cubic meter": 1,
            "Teaspoon (US)": 4.92892e-6,
            "Tablespoon (US)": 1.47868e-5,
            "Fluid ounce (US)": 2.95735e-5,
            "Cup (US)": 2.36588e-4,
            "Pint (US)": 4.73176e-4,
            "Quart (US)": 9.46353e-4,
            "Gallon (US)": 0.00378541,
            "Cubic inch": 1.63871e-5,
            "Cubic foot": 0.0283168,
            "Cubic yard": 0.764555
        },
        "Area": {
            "Square millimeter": 1e-6,
            "Square centimeter": 1e-4,
            "Square meter": 1,
            "Hectare": 10000,
            "Square kilometer": 1e6,
            "Square inch": 0.00064516,
            "Square foot": 0.092903,
            "Square yard": 0.836127,
            "Acre": 4046.86,
            "Square mile": 2.59e6
        },
        "Speed": {
            "Meter per second": 1,
            "Kilometer per hour": 0.277778,
            "Mile per hour": 0.44704,
            "Knot": 0.514444,
            "Foot per second": 0.3048
        },
        "Time": {
            "Nanosecond": 1e-9,
            "Microsecond": 1e-6,
            "Millisecond": 1e-3,
            "Second": 1,
            "Minute": 60,
            "Hour": 3600,
            "Day": 86400,
            "Week": 604800,
            "Month": 2.628e6,
            "Year": 3.154e7,
            "Decade": 3.154e8,
            "Century": 3.154e9
        }
    }
    
    # Main container
    with st.container():
        st.markdown('<div class="converter-card">', unsafe_allow_html=True)
        
        # Title
        st.markdown('<h2 class="header">Unit Converter</h2>', unsafe_allow_html=True)
        
        # Conversion type selector
        conversion_type = st.selectbox("Select conversion type", list(conversion_types.keys()))
        units = conversion_types[conversion_type]
        
        # Create two columns for input and output
        col1, col2 = st.columns(2)
        
        with col1:
            from_unit = st.selectbox("From", list(units.keys()), key="from")
            input_value = st.number_input("", value=1.0, format="%.6f", key="input")
            
        with col2:
            to_unit = st.selectbox("To", list(units.keys()), key="to")
            output_value = convert_units(input_value, from_unit, to_unit, conversion_type, conversion_types)
            st.markdown(f'<div class="result">{output_value:.6g}</div>', unsafe_allow_html=True)           

        if conversion_type != "Temperature" and from_unit != to_unit:
            formula = f"1 {from_unit} = {units[from_unit]/units[to_unit]:.6g} {to_unit}"
            st.markdown(f"<div class='unit-label'>{formula}</div>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:  # from_unit is already Celsius
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return celsius * 9/5 + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:  # to_unit is Celsius
        return celsius

if __name__ == "__main__":
    main()