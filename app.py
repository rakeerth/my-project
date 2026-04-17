import streamlit as st

st.title("Weather App")

# Input field
city = st.text_input("Enter city name:")

# Button
if st.button("Get current Weather "):
    if city:
        weather = f"Weather in {city}: 🌤️ 30°C, Clear Sky"
        st.success(weather)
    else:
        st.warning("Please enter a city name")
