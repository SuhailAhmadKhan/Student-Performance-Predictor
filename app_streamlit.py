import streamlit as st
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Create a Streamlit web app
st.title('Student Performance Predictor')

# Define a function to get user input and make predictions
def predict_datapoint():
    st.header("Predict Data Point")
    
    # Create form to collect user input
    with st.form(key='prediction_form'):
        gender = st.radio("Gender", ["male", "female"])
        ethnicity = st.selectbox("Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        parental_education = st.selectbox("Parental Education", ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"])
        lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
        test_preparation = st.selectbox("Test Preparation Course", ["none", "completed"])
        reading_score = st.slider("Reading Score", min_value=0, max_value=100, value=50)
        writing_score = st.slider("Writing Score", min_value=0, max_value=100, value=50)

        # Submit button
        submit_button = st.form_submit_button(label='Predict')

    # Display prediction results if the form is submitted
    if submit_button:
        try:
            # Create CustomData object
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_education,
                lunch=lunch,
                test_preparation_course=test_preparation,
                reading_score=float(reading_score),
                writing_score=float(writing_score)
            )

            # Get data as a DataFrame
            pred_df = data.get_data_as_data_frame()

            # Make predictions using the PredictPipeline
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            # Display the results
            st.subheader("Prediction Results:")
            st.write(results[0])

        except Exception as e:
            # Print the error message
            st.error(f"An error occurred: {str(e)}")

# Call the function to predict datapoint
predict_datapoint()
