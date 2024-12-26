import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model
model = load('eniyi.joblib')

# Get the expected feature names from the model
expected_features = model.feature_names_in_

# Streamlit app title
st.title("Cybersecurity Risk Detector")

# Input fields for user data
st.header("Enter System Details")
num_vulnerabilities = st.number_input("Number of Vulnerabilities", min_value=0, max_value=100, step=1)
system_uptime = st.number_input("System Uptime (days)", min_value=0, max_value=1000, step=1)
num_security_incidents = st.number_input("Number of Security Incidents", min_value=0, max_value=50, step=1)
patch_frequency = st.selectbox("Patch Update Frequency", ["Weekly", "Monthly", "Rarely"])  # Drop 'Daily'
num_open_ports = st.number_input("Number of Open Ports", min_value=1, max_value=65535, step=1)

# Prepare the input data
input_data_dict = {
    'Number of Vulnerabilities': [num_vulnerabilities],
    'System Uptime (days)': [system_uptime],
    'Number of Security Incidents': [num_security_incidents],
    'Patch Update Frequency_Weekly': [1 if patch_frequency == 'Weekly' else 0],
    'Patch Update Frequency_Monthly': [1 if patch_frequency == 'Monthly' else 0],
    'Patch Update Frequency_Rarely': [1 if patch_frequency == 'Rarely' else 0],
    'Number of Open Ports': [num_open_ports]
}

# Reorder input data to match the model's expected features
input_data = pd.DataFrame(input_data_dict)
input_data = input_data.reindex(columns=expected_features, fill_value=0)  # Ensure correct order and fill missing features with 0

# Predict button
if st.button("Predict Risk Level"):
    try:
        # Debug: Print input data
        st.write("Input Data:", input_data)
        
        prediction = model.predict(input_data)
        
        # Debug: Print prediction result
        st.write("Prediction Result:", prediction)
        
        risk_level = "High Risk" if prediction[0] == 1 else "Low Risk"
        st.subheader(f"Predicted Risk Level: {risk_level}")
    except Exception as e:
        st.error(f"An error occurred: {e}")