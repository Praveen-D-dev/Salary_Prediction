import streamlit as s
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Page title
s.title("💼 Salary Prediction App")

# CSS for dark theme glowing border box
s.markdown("""
    <style>
    .glow-box {
        background-color: #1e1e1e;
        border: 2px solid #00ff88;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 0 20px #00ff88;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Wrap form content inside styled box
s.markdown('<div class="glow-box">', unsafe_allow_html=True)

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

s.markdown('</div>', unsafe_allow_html=True)
