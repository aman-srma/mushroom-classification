import streamlit as st
import os
import numpy as np
from MushroomClassification.pipeline.prediction import PredictionPipeline

st.set_page_config(
    page_title="Mushroom Classification",
    page_icon="🍄",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Mushroom Classification")

# Sidebar
st.sidebar.header("Navigation")
app_mode = st.sidebar.selectbox("Choose an option", ["Home", "Train Model", "Predict"])

if app_mode == "Home":
    st.write("Welcome to the Mushroom Classification App!")

if app_mode == "Train Model":
    if st.button("Train Model"):
        os.system("python main.py")
        st.success("Training Successful!")

if app_mode == "Predict":
    st.write("Fill in the mushroom features to make a prediction:")
    # Define input fields
    cap_shape = st.selectbox("Cap Shape", list(range(1, 11)))
    cap_surface = st.selectbox("Cap Surface", list(range(1, 11)))
    cap_color = st.selectbox("Cap Color", list(range(1, 11)))
    bruises = st.selectbox("Bruises", list(range(1, 11)))
    odor = st.selectbox("Odor", list(range(1, 11)))
    gill_attachment = st.selectbox("Gill Attachment", list(range(1, 11)))
    gill_spacing = st.selectbox("Gill Spacing", list(range(1, 11)))
    gill_size = st.selectbox("Gill Size", list(range(1, 11)))
    gill_color = st.selectbox("Gill Color", list(range(1, 11)))
    stalk_shape = st.selectbox("Stalk Shape", list(range(1, 11)))
    stalk_surface_above_ring = st.selectbox("Stalk Surface Above Ring", list(range(1, 11)))
    stalk_surface_below_ring = st.selectbox("Stalk Surface Below Ring", list(range(1, 11)))
    stalk_color_above_ring = st.selectbox("Stalk Color Above Ring", list(range(1, 11)))
    stalk_color_below_ring = st.selectbox("Stalk Color Below Ring", list(range(1, 11)))
    veil_color = st.selectbox("Veil Color", list(range(1, 11)))
    ring_number = st.selectbox("Ring Number", list(range(1, 11)))
    ring_type = st.selectbox("Ring Type", list(range(1, 11)))
    spore_print_color = st.selectbox("Spore Print Color", list(range(1, 11)))
    population = st.selectbox("Population", list(range(1, 11)))
    habitat = st.selectbox("Habitat", list(range(1, 11)))

    # Create a feature list
    feature_list = [
        cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment, gill_spacing, gill_size, gill_color,
        stalk_shape, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring,
        veil_color, ring_number, ring_type, spore_print_color, population, habitat
    ]
    features = np.array(feature_list).reshape(1, -1)

    if st.button("Predict"):
        obj = PredictionPipeline()
        predict = obj.predict(features)
        result = {0: "edible", 1: "poisonous"}
        st.success(f"Prediction: {result[predict]}")