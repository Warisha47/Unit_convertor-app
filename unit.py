import streamlit as st 

st.title("🌎 Unit Converter App")
st.markdown("## Converts Length, Weight, Time ,Temperature instantly")
st.write(" Welcome! Select a Category, enter a value and get the converted result instantly.")
st.markdown("""
    <style>
        div.stButton > button:first-child {
            background-color:rgb(109, 76, 175);
            color: white;
            width: 200px;
            height: 50px;
            font-size: 18px;
            border-radius: 10px;
            transition: background-color 0.3s ease;
        }
        
        div.stButton > button:first-child:hover {
            background-color:rgb(51, 228, 255); /* Change color on hover */
            color: white;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)
import streamlit as st

st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to right, #e3f2fd, #f8bbd0);
        }
    </style>
""", unsafe_allow_html=True)



category=st.selectbox("Choose a Category", ["📏Length", "⚖️Weight", "🧭Time", "🌡️Temperature"])

def convert_units(category,value,unit):
    if category=="📏Length":
        if unit== "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
        elif unit == "Inch to yard":
           return value /36
        
        elif unit == "Yard to inch":
            return value * 36
        
        elif unit == "Inch to Meter":
           return value / 39.37
        
        elif unit == "Meter to Inch":
           return value * 39.37
           
        
    elif category=="⚖️Weight":
        if unit== "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilogram":
            return value / 2.20462

    elif category == "🧭Time":
        if unit=="Seconds to minutes":
            return value /60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

    elif category == "🌡️Temperature":
        if unit == "Celcius to Fahrheneite":
            return value* 9/5 + 32
        elif unit == "Fahrheneit to celcius":
            return (value-32)* 5/9    

    return 0       
            
if category=="📏Length":
 unit=st.selectbox("Select Conversion",["Kilometers to miles", "Miles to Kilometers" ,"Inch to yard","Yard to inch" , "Inch to Meter","Meter to Inch"])

elif category=="⚖️Weight":
 unit=st.selectbox("Select Conversion",["Kilograms to Pounds","Pounds to Kilogram"]) 

elif category=="🧭Time":
 unit=st.selectbox("Select conversion",["Seconds to minutes","Minutes to seconds","Minutes to hours", "Hours to minutes","Hours to days","Days to hours"])  

elif category=="🌡️Temperature":
 unit=st.selectbox("Select conversion",["Celcius to Fahrheneite","Fahrheneit to celcius"])


value = st.number_input("Enter the value to convert")          

if st.button("Convert"):
    result=convert_units(category,value,unit)
    st.success(f"The result is {result:.2f}")