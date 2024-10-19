import streamlit as st
import joblib

# Load your model
model = joblib.load('path_to_your_model/final_modell.joblib')  # Replace 'path_to_your_model' with the actual path

st.title("Travel Experience Recommendation")

# User inputs for preferences
temperature = st.slider("Preferred Average Temperature", min_value=0, max_value=40)
attractions = st.number_input("Number of Tourist Attractions", min_value=0)
accommodation_cost = st.number_input("Accommodation Cost", min_value=0)
transportation_cost = st.number_input("Transportation Cost", min_value=0)
cuisine_diversity = st.selectbox("Cuisine Diversity", ["Low", "Moderate", "High"])
safety_rating = st.slider("Safety Rating", min_value=1, max_value=10)
nightlife_rating = st.slider("Nightlife Rating", min_value=1, max_value=10)
outdoor_activities = st.selectbox("Outdoor Activities Available", ["Yes", "No"])
cultural_heritage = st.selectbox("Cultural Heritage Sites", ["Yes", "No"])

# Prepare input for model
input_data = [[temperature, attractions, accommodation_cost, transportation_cost, cuisine_diversity, safety_rating, nightlife_rating, outdoor_activities, cultural_heritage]]

# Make prediction
if st.button("Get Travel Experience Recommendation"):
    prediction = model.predict(input_data)
    st.write(f"Recommended Travel Experience: {prediction[0]}")
