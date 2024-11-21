import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
import os

model_path = os.path.join(os.path.dirname(__file__), "logistic_regression_model_health.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)


st.title("Medical Test Results Classification")
st.write("This app classifies test results into Normal, Inconclusive, or Abnormal using Logistic Regression Model.")

st.subheader("Enter Patient Information")


age = st.number_input("Age", min_value=0, max_value=120)
Days = st.number_input("Days",min_value=0)
gender = st.selectbox("Gender",['Male','Female'])
blood_type = st.selectbox("Blood Type", ['A+','A-','B+','B-','AB+','AB-','O+','O-'])
medical_condition = st.selectbox("Medical Condition",['Cancer','Obesity','Diabetes','Asthma','Hypertension','Arthritis'])
admission_type = st.selectbox("Admission Type",['Urgent','Emergency','Elective'])
medication = st.selectbox("Medication",['Paracetamol','Ibuprofen','Aspirin','Penicillin','Lipitor'])


input = pd.DataFrame({
    'Age':[age],
    'Days':[Days],
    'Gender_Male':[1 if gender == 'Male' else 0],
    'Blood Type_A-':[1 if blood_type == 'A-' else 0],
    'Blood Type_AB+':[1 if blood_type == 'AB+' else 0],
    'Blood Type_AB-':[1 if blood_type == 'AB-' else 0],
    'Blood Type_B+':[1 if blood_type == 'B+' else 0],
    'Blood Type_B-':[1 if blood_type == 'B-' else 0],
    'Blood Type_O+':[1 if blood_type == 'O+' else 0],
    'Blood Type_O-':[1 if blood_type == 'O-' else 0],
    'Medical Condition_Asthma':[1 if medical_condition == 'Asthma' else 0],
    'Medical Condition_Cancer':[1 if medical_condition == 'Cancer' else 0],
    'Medical Condition_Diabetes':[1 if medical_condition == 'Diabetes' else 0],
    'Medical Condition_Hypertension':[1 if medical_condition == 'Hypertension' else 0],
    'Medical Condition_Obesity':[1 if medical_condition == 'Onesity' else 0],
    'Admission Type_Emergency':[1 if admission_type == 'Emergency' else 0],
    'Admission Type_Urgent':[1 if admission_type == 'Urgent' else 0],
    'Medication_Ibuprofen':[1 if medication == 'Ibuprofen' else 0],
    'Medication_Lipitor':[1 if medication == 'Lipitor' else 0],
    'Medication_Paracetamol':[1 if medication == 'Paracetamol' else 0],
    'Medication_Penicillin':[1 if medication == 'Penicillin' else 0]
})


expected_order = ['Age', 'Days', 'Gender_Male', 'Blood Type_A-',
       'Blood Type_AB+', 'Blood Type_AB-', 'Blood Type_B+', 'Blood Type_B-',
       'Blood Type_O+', 'Blood Type_O-', 'Medical Condition_Asthma',
       'Medical Condition_Cancer', 'Medical Condition_Diabetes',
       'Medical Condition_Hypertension', 'Medical Condition_Obesity',
       'Admission Type_Emergency', 'Admission Type_Urgent',
       'Medication_Ibuprofen', 'Medication_Lipitor', 'Medication_Paracetamol',
       'Medication_Penicillin']

input_data = input.reindex(columns=expected_order)

if st.button('predict'):
    predict = model.predict(input_data)
    maping = {0:'Normal',2:'Inconclusive',1:'Abnormal'}
    result = maping[predict[0]]
    st.write(f'The Predicted Test Result is **{result}**')

