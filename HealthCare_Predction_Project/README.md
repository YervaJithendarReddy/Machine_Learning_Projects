# Healthcare Classification Prediction Project

**NOTE**
- "Due to the synthetic nature and limitations of the dataset (e.g., imbalanced classes, missing features, and lack of real-world variability), the model's accuracy was constrained. However, the project focused on understanding key factors, preprocessing techniques, and evaluating the model's behavior in such scenarios, providing valuable insights into predictive modeling under challenging conditions."

# Problem Statement:

The objective of this project is to develop a machine learning model to assess a patient's health condition based on various medical and demographic features. The model aims to classify the health status into one of three categories: Normal, Abnormal, or Inconclusive.

The solution will leverage patient data, including vital signs, diagnostic results, and medical history, to assist healthcare providers in prioritizing attention to critical cases and improving decision-making efficiency. The model should achieve high accuracy while ensuring interpretability to gain trust from healthcare professionals.

## 🚀 Project Overview

This project focuses on predicting healthcare outcomes using machine learning techniques. By leveraging patient data, the model classifies conditions (e.g., disease diagnosis, risk assessment) to assist in better decision-making. 

The project is built with **Python** and integrates key libraries for data preprocessing, visualization, and modeling.

---

## 📊 Key Features

- **Data Analysis**: Exploratory Data Analysis (EDA) to uncover insights and trends in the healthcare dataset.  
- **Preprocessing**: Handling missing values, encoding categorical variables, scaling numerical features, and dealing with outliers.
- **Model Building**: Implementation of classification algorithms, including Logistic Regression, Random Forest, and XGBoost.
- **Evaluation**: Comprehensive model evaluation using metrics such as accuracy, precision, recall, F1-score, and AUC-ROC.
- **Deployment**: Deployed the model after training using Streamlit(a python library) to transfer the model from an Development enviroment to Production Environment.

## 📊 About Dataset
**Context**:
This synthetic healthcare dataset has been created to serve as a valuable resource for data science, machine learning, and data analysis enthusiasts. It is designed to mimic real-world healthcare data, enabling users to practice, develop, and showcase their data manipulation and analysis skills in the context of the healthcare industry.

**Inspiration**:
The inspiration behind this dataset is rooted in the need for practical and diverse healthcare data for educational and research purposes. Healthcare data is often sensitive and subject to privacy regulations, making it challenging to access for learning and experimentation. To address this gap, I have leveraged Python's Faker library to generate a dataset that mirrors the structure and attributes commonly found in healthcare records. By providing this synthetic data, I hope to foster innovation, learning, and knowledge sharing in the healthcare analytics domain.

**Dataset Information**:
Each column provides specific information about the patient, their admission, and the healthcare services provided, making this dataset suitable for various data analysis and modeling tasks in the healthcare domain. Here's a brief explanation of each column in the dataset -

Name: This column represents the name of the patient associated with the healthcare record.
Age: The age of the patient at the time of admission, expressed in years.
Gender: Indicates the gender of the patient, either "Male" or "Female."
Blood Type: The patient's blood type, which can be one of the common blood types (e.g., "A+", "O-", etc.).
Medical Condition: This column specifies the primary medical condition or diagnosis associated with the patient, such as "Diabetes," "Hypertension," "Asthma," and more.
Date of Admission: The date on which the patient was admitted to the healthcare facility.
Doctor: The name of the doctor responsible for the patient's care during their admission.
Hospital: Identifies the healthcare facility or hospital where the patient was admitted.
Insurance Provider: This column indicates the patient's insurance provider, which can be one of several options, including "Aetna," "Blue Cross," "Cigna," "UnitedHealthcare," and "Medicare."
Billing Amount: The amount of money billed for the patient's healthcare services during their admission. This is expressed as a floating-point number.
Room Number: The room number where the patient was accommodated during their admission.
Admission Type: Specifies the type of admission, which can be "Emergency," "Elective," or "Urgent," reflecting the circumstances of the admission.
Discharge Date: The date on which the patient was discharged from the healthcare facility, based on the admission date and a random number of days within a realistic range.
Medication: Identifies a medication prescribed or administered to the patient during their admission. Examples include "Aspirin," "Ibuprofen," "Penicillin," "Paracetamol," and "Lipitor."
Test Results: Describes the results of a medical test conducted during the patient's admission. Possible values include "Normal," "Abnormal," or "Inconclusive," indicating the outcome of the test.
Usage Scenarios:
This dataset can be utilized for a wide range of purposes, including:

Developing and testing healthcare predictive models.
Practicing data cleaning, transformation, and analysis techniques.
Creating data visualizations to gain insights into healthcare trends.
Learning and teaching data science and machine learning concepts in a healthcare context.
You can treat it as a Multi-Class Classification Problem and solve it for Test Results which contains 3 categories(Normal, Abnormal, and Inconclusive).
**Acknowledgments**:
I acknowledge the importance of healthcare data privacy and security and emphasize that this dataset is entirely synthetic. It does not contain any real patient information or violate any privacy regulations.
I hope that this dataset contributes to the advancement of data science and healthcare analytics and inspires new ideas. Feel free to explore, analyze, and share your findings with the Kaggle community.



Thank You! 😊

**Connect With me ON**

[`Linkedin`](!https://www.linkedin.com/in/y-jithendar-reddy)
