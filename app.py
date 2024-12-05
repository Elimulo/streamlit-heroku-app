import streamlit as st
import requests

# Define the URL of your deployed Flask app on Heroku
url = "https://p7prediction-c1a4ba9f54fa.herokuapp.com/predict"

# Streamlit interface
st.title("Credit Default Prediction")

# Input form for client data
client_data = {}
client_data['REGION_RATING_CLIENT_W_CITY'] = st.number_input('Enter REGION_RATING_CLIENT_W_CITY', min_value=0, max_value=100)

# Add other necessary inputs for your model here (for example, if you have more features)
# client_data['feature_2'] = st.number_input('Enter feature_2', min_value=0, max_value=100)

if st.button("Get Prediction"):
    # Prepare the payload
    payload = {"client_data": client_data}

    # Send the POST request
    response = requests.post(url, json=payload)

    # Check if the response is successful
    if response.status_code == 200:
        prediction = response.json()
        prob = prediction['probabilité_defaut']
        client_class = prediction['classe']
        # Display the result
        st.write(f"Probability of Default: {prob}")
        st.write(f"Class: {client_class}")
    else:
        st.write(f"Error: {response.status_code}, {response.text}")
