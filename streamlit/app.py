import streamlit as st
import requests

st.title("Travel Destination Recommendation")

# Input fields for user preferences
average_temperature = st.number_input("Average Temperature")
tourist_attractions = st.number_input("Number of Tourist Attractions")
accommodation_cost = st.number_input("Accommodation Cost")
transportation_cost = st.number_input("Transportation Cost")
# Add more input fields as needed...

if st.button("Get Recommendation"):
    # Prepare data to send to Django
    payload = {
        'average_temperature': average_temperature,
        'tourist_attractions': tourist_attractions,
        'accommodation_cost': accommodation_cost,
        'transportation_cost': transportation_cost,
        # Include other fields...
    }
    
    # Send request to Django API
    response = requests.post("http://127.0.0.1:8000/api/recommend/", json=payload)

    if response.status_code == 200:
        recommendation = response.json().get('recommendation')
        st.success(f"We recommend: {recommendation}")
    else:
        st.error("Failed to get recommendation.")
