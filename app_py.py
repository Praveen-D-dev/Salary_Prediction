# -*- coding: utf-8 -*-
import streamlit as s
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title
s.title("💼 Salary Prediction App")

# 🔲 Add custom CSS for border and background
s.markdown("""
    <style>
    .prediction-box {
        background-color: #f0f8ff;
        border: 3px solid #4CAF50;
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 🧩 Add the form inside a styled div
s.markdown('<div class="prediction-box">', unsafe_allow_html=True)

age = s.number_input("👤 Age", min_value=18, max_value=60)
gender = s.selectbox("🚻 Gender", ("Male", "Female"))
gender = 1 if gender == "Male" else 0

education_level = s.selectbox("🎓 Education Level", ("Bachelor", "Master", "PhD"))
education_level = {"Bachelor": 0, "Master": 1, "PhD": 2}[education_level]

years_of_experience = s.number_input("💼 Years of Experience", min_value=0, max_value=30)

if s.button("🔮 Predict"):
    data = np.array([[age, gender, education_level, years_of_experience]])
    prediction = model.predict(data)
    s.success(f"💰 The predicted salary is ₹{prediction[0]:,.2f}")

s.markdown('</div>', unsafe_allow_html=True)  # Close custom div
