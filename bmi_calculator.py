import streamlit as st

# Inject CSS to style the app
st.markdown("""
    <style>
    .title {
        font-size: 3em;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .input {
        font-size: 1.5em;
        margin-top: 20px;
    }
    .result {
        font-size: 2em;
        color: #FFA500;
        text-align: center;
        margin-top: 20px;
    }
    .category {
        font-size: 1.5em;
        margin-top: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the app
st.markdown('<p class="title">BMI Calculator</p>', unsafe_allow_html=True)

# Input fields for height in centimeters and weight in kilograms
height_cm = st.number_input("Enter your height in centimeters:", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight in kilograms:", min_value=0.0, format="%.2f")

# Submit button
if st.button('Calculate BMI'):
    if height_cm > 0 and weight > 0:
        # Convert height from centimeters to meters
        height_m = height_cm / 100.0
        
        # Calculate BMI
        bmi = weight / (height_m ** 2)
        st.markdown(f'<p class="result">BMI Calculated is: {bmi:.2f}</p>', unsafe_allow_html=True)

        # Determine BMI category
        if bmi <= 16:
            st.markdown('<p class="category">You are very underweight</p>', unsafe_allow_html=True)
        elif bmi <= 18.5:
            st.markdown('<p class="category">You are underweight</p>', unsafe_allow_html=True)
        elif bmi <= 25:
            st.markdown('<p class="category">Congrats! You are healthy</p>', unsafe_allow_html=True)
        elif bmi <= 30:
            st.markdown('<p class="category">You are overweight</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="category">You are very overweight</p>', unsafe_allow_html=True)
    else:
        if height_cm <= 0:
            st.write("Please enter a valid height.")
        if weight <= 0:
            st.write("Please enter a valid weight.")
