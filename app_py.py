import streamlit as s
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Page title
s.title("💼 Salary Prediction App")

# CSS for glowing bordered container
s.markdown("""
    <style>
    .full-box {
        background-color: #1e1e1e;
        border: 2px solid #00ff88;
        border-radius: 15px;
        box-shadow: 0 0 15px #00ff88;
        padding: 30px;
        margin-top: 30px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Start of bordered container
s.markdown('<div class="full-box">', unsafe_allow_html=True)

# All inputs inside the box
age = s.number_input("👤 Age", min_value=18, max_value=60)
gender = s.selectbox("🚻 Gender", ("Male", "Female"))
gender = 1 if gender == "Male" else 0

education_level = s.selectbox("🎓 Education Level", ("Bachelor", "Master", "PhD"))
education_level = {"Bachelor": 0, "Master": 1, "PhD": 2}[education_level]

years_of_experience = s.number_input("💼 Years of Experience", min_value=0, max_value=30)

# Predict button also inside the same box
if s.button("🔮 Predict"):
    data = np.array([[age, gender, education_level, years_of_experience]])
    prediction = model.predict(data)
    s.success(f"💰 The predicted salary is ₹{prediction[0]:,.2f}")

# End of bordered container
s.markdown('</div>', unsafe_allow_html=True)
