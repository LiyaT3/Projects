# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:51:30 2024

@author: LIYA
"""

import pickle 
import io
import streamlit as st
from streamlit_option_menu import option_menu


#Since these files have a different encoding style, going forward with io,where discrepancy issues are less

file_path = 'C:/Users/ADMIN/Desktop/AISPRY/PROJECT_TRIAL/multiple_disease_pred/saved_models/diabetes.pkl'
with io.open(file_path, 'rb') as file:
    diabetes_model =pickle.load(file)
    
file_path_heart ='C:/Users/ADMIN/Desktop/AISPRY/PROJECT_TRIAL/multiple_disease_pred/saved_models/heart.pkl'
with io.open(file_path_heart, 'rb') as heart_file:
    heart_model=pickle.load(heart_file)
    
    
file_path_can ='C:/Users/ADMIN/Desktop/AISPRY/PROJECT_TRIAL/multiple_disease_pred/saved_models/breast_cancer.pkl'
with io.open(file_path_can, 'rb') as can_file:
    cancer_model=pickle.load(can_file)


#Creating the navigation bar and creating 3 different webpages   
with st.sidebar:
    selected = option_menu('Multiple Disease Predictor', ['Diabetes Predictor'
                                                          ,'Heart Disease Predictor', 
                                                          'Breast Cancer Predictor'],
                           icons =['eyedropper', 'heart-pulse-fill', 'virus'], #Bootstarp Icons
                           default_index =0) #Deafult page would be in diabetes
#Since all different pages , if selected
if selected == 'Diabetes Predictor':
    #Page Title
    st.title('Diabetes Predictor using ML')
    
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col4:
        SkinThickness = st.text_input('Skin Thickeness Value')
    with col1:
        Insulin = st.text_input('Insulin level')
    with col2:
        BMI =st.text_input('BMI Value')
    with col3:
        DiabetesPedigreeFunction =st.text_input('Diabetes Pedigree Function Value')
    with col4:
        Age = st.text_input('Age of the person')
    #Code for prediction
    diab_diag =' '
    #Doing for on val , go with [[]] ,creating a button
    if st.button('Diabetes Test Results'):
        diab_pred  = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age  ]])
        if diab_pred[0]==1:
            diab_diag = 'The person is diabetic'
            
        else:
            diab_diag = 'The person is not diabetic'
    st.success(diab_diag)   
    
    
if selected == 'Heart Disease Predictor':
    # Page Title
    st.title('Heart Predictor using ML')

    # Input variables
    age = st.text_input('Age of the person')
    sex = st.text_input('Sex of the person')
    cp = st.text_input('Chest Pain Type')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Cholestoral')
    fbs = st.text_input('Fasting Blood Sugar')
    restecg = st.text_input('Resting ECG')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST Depression induced by exercise relative to rest')
    slope = st.text_input('Heart Rate Slope')
    ca = st.text_input('Number of Major Vessels (0-3) colored by Flourosopy')
    thal = st.text_input('Thalassemia')

    heart_diag = ''

    try:
        # Convert input variables to numeric format with improved data validation
        input_var = [
            float(age) if age.strip() else 0.0,
            float(sex) if sex.strip() else 0.0,
            float(cp) if cp.strip() else 0.0,
            float(trestbps) if trestbps.strip() else 0.0,
            float(chol) if chol.strip() else 0.0,
            float(fbs) if fbs.strip() else 0.0,
            float(restecg) if restecg.strip() else 0.0,
            float(thalach) if thalach.strip() else 0.0,
            float(exang) if exang.strip() else 0.0,
            float(oldpeak) if oldpeak.strip() else 0.0,
            float(slope) if slope.strip() else 0.0,
            float(ca) if ca.strip() else 0.0,
            float(thal) if thal.strip() else 0.0
        ]

        if st.button('Heart Disease Results'):
            heart_diag = heart_model.predict([input_var])
            if heart_diag[0] == 1:
                heart_diag = 'The patient has a heart disease'
            else:
                heart_diag = 'The patient is healthy'
    except ValueError:
        st.error('Please enter valid numeric values for all input fields.')

    st.success(heart_diag)
      
    
if selected == 'Breast Cancer Predictor':
    
    #Page Title
    st.title('Breast Cancer Predictor using ML')
    
    
    mean_radius = st.text_input('Radius')
    mean_texture = st.text_input('Texture ')
    mean_perimeter = st.text_input('Perimeter')
    mean_area = st.text_input('Area')
    mean_smoothness = st.text_input('Smoothness')
    mean_compactness = st.text_input('Compactness')
    mean_concavity = st.text_input('Concavity')
    mean_concave_points = st.text_input('Concave Points')
    mean_symmetry = st.text_input('Symmetry')
    mean_fractal_dimension = st.text_input('Fractal Dimension')

    radius_error = st.text_input('Radius Error')
    texture_error = st.text_input('Texture Error')
    perimeter_error = st.text_input('Perimeter Error')
    area_error = st.text_input('Area Error')
    smoothness_error = st.text_input('Smoothness Error')
    compactness_error = st.text_input('Compactness Error')
    concavity_error = st.text_input('Concavity Error')
    concave_points_error = st.text_input('Concave Points Error')
    symmetry_error = st.text_input('Symmetry Error')
    fractal_dimension_error = st.text_input('Fractal Dimension Error')

    worst_radius = st.text_input('Worst Radius')
    worst_texture = st.text_input('Worst Texture')
    worst_perimeter = st.text_input('Worst Perimeter')
    worst_area = st.text_input('Worst Area')
    worst_smoothness = st.text_input('Worst Smoothness')
    worst_compactness = st.text_input('Worst Compactness')
    worst_concavity = st.text_input('Worst Concavity')
    worst_concave_points = st.text_input('Worst Concave Points')
    worst_symmetry = st.text_input('Worst Symmetry')
    worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    inp_var2 = [ mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
    mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
    radius_error, texture_error, perimeter_error, area_error, smoothness_error,
    compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error,
    worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
    worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]

    canc_diag =''
    
    if st.button('Breast Cancer Predictor'):
        
        cancer_pred = cancer_model.predict([inp_var2])
        
        if cancer_pred[0]==1:
            canc_diag = 'The tumor is benign'
        else:
            canc_diag = 'The tumor is malignant'
    st.success(canc_diag)
        
