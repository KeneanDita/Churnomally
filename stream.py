import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")


st.title("Churn Prediction App")

st.divider()

st.write("Please enter the following details and hit the predict button to get the churn prediction.")

st.divider()

age = st.number_input("Age", min_value=10, max_value=100, value=30)
tenure = st.number_input("Tenure", min_value=0, max_value=130,value=12)
mothly_charges = st.number_input("Monthly Charges", min_value=30, max_value=150)
gender = st.selectbox("Gender", ["Male", "Female"])


st.divider()

predict_button = st.button("Predict")
st.divider()

if predict_button:
    gender_selected = 1 if gender == "Female" else 0
    X = [age, gender_selected, tenure, mothly_charges]
    X1 = np.array(X)

    X_array = scaler.transform([X1])
    prediction = model.predict(X_array)[0]
    predicted = "Yes" if prediction == 1 else "No"
    st.snow()
    st.write(f"Predicted(Churn): {predicted}")

else:
    st.write("Please fill in all the fields and click the predict button.")