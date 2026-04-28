import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title(" Archaeological Site Predictor")

st.write("Enter location features to predict if the area may contain archaeological ruins.")

# Inputs
distance = st.slider("Distance from Nile (km)", 0.0, 15.0, 2.0)
elevation = st.slider("Elevation (meters)", 0, 150, 50)

# Prediction
if st.button("Predict"):
    prediction = model.predict([[distance, elevation]])

    if prediction[0] == 1:
        st.success("High probability of archaeological site ")
    else:
        st.error("Low probability of archaeological site ")
