import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Custom CSS for light healthcare-friendly theme
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f5fafd;
        color: #000000;
    }
    .sidebar .sidebar-content {
        background-color: #f2f9ff;
    }
    .stButton > button {
        background-color: #4fc3f7;
        color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #039be5;
    }
    .title {
        font-size: 36px;
        color: #0d47a1;
        text-align: center;
        padding: 20px;
        font-weight: bold;
    }
    .vit-banner {
        font-size: 48px;
        color: #1a237e;
        text-align: center;
        padding: 20px;
        background-color: #e3f2fd;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        font-family: 'Arial', sans-serif;
    }
    .about-us {
        font-size: 18px;
        color: #000000;
        padding: 20px;
        text-align: center;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTextInput input {
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #cccccc;
        background-color: #ffffff;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.markdown("### 🩺 Prognosis Menu")
    selected = option_menu('Select Prediction Type:',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'About Us'],
                           icons=['activity', 'heart', 'person', 'info'],
                           default_index=0,
                           styles={
                               "container": {"padding": "5!important", "background-color": "#f2f9ff"},
                               "icon": {"color": "#2c3e50", "font-size": "20px"},
                               "nav-link": {
                                   "font-size": "18px",
                                   "text-align": "left",
                                   "margin": "0px",
                                   "--hover-color": "#d1eaf0"
                               },
                               "nav-link-selected": {"background-color": "#bbdefb", "color": "#000000"},
                           })

# # Display VIT banner
# st.markdown('<div class="vit-banner">Prognosis</div>', unsafe_allow_html=True)

# Display VIT banner with logo
st.markdown('<div class="vit-banner"><img src="https://img.icons8.com/fluency/48/stethoscope.png" alt="logo"/>Prognosis</div>', unsafe_allow_html=True)

# About Us
if selected == 'About Us':
    st.markdown("## ℹ️ About Us")
    st.markdown("""
        <div class="about-us">
            <p><strong>Prognosis</strong> is an advanced predictive analytics application designed to provide accurate predictions for various health conditions. By leveraging machine learning models, Prognosis helps users assess the likelihood of diabetes, heart disease, and Parkinson's disease based on their input data.</p>
            <p>This project aims to offer a user-friendly interface that integrates powerful prediction models in a single platform, making health assessments more accessible and reliable. This is My project-II for Vellore Institute of Technology.</p>
            <p><strong>Creators:</strong><br>
             Purshottam Mehta<br>
        </div>
    """, unsafe_allow_html=True)

# Input conversion helper
def safe_float_input(input_value, default_value=0.0):
    try:
        return float(input_value)
    except ValueError:
        return default_value

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.markdown("## 🦠 Diabetes Prediction")
    st.markdown("Fill in the following details to check the likelihood of diabetes.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = safe_float_input(st.text_input('No. of Pregnancies?'))
    with col2:
        Glucose = safe_float_input(st.text_input('Glucose Level?'))
    with col3:
        BloodPressure = safe_float_input(st.text_input('Blood Pressure?'))
    with col1:
        SkinThickness = safe_float_input(st.text_input('Skin Thickness?'))
    with col2:
        Insulin = safe_float_input(st.text_input('Insulin?'))
    with col3:
        BMI = safe_float_input(st.text_input('BMI?'))
    with col1:
        DiabetesPedigreeFunction = safe_float_input(st.text_input('Diabetes Pedigree Function value?'))
    with col2:
        Age = safe_float_input(st.text_input('Age?'))

    diab_diagnosis = ''
    diab_advice = ''

    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic :( 🨧'
                diab_advice = """
                    **Advice-:**
                    - Maintain a healthy and balanced diet.
                    - Monitor blood sugar levels regularly.
                    - Exercise daily for 30 minutes.
                    - Take medications as prescribed.
                    - Prioritize sleep and stress management.
                """
            else:
                diab_diagnosis = 'The person is not diabetic :) 😁'
                diab_advice = """
                    ***Tips - Prevention is better than cure :)***
                    - Stay active and eat well.
                    - Continue eating a balanced diet.
                   - Stay physically active with regular exercise.
                   - Avoid smoking and manage stress effectively.
                   - Maintain a healthy weight and get body tests occassionly done.
                   - Sleep is important!!
                """
        except Exception as e:
            diab_diagnosis = f"Error in prediction: {str(e)}"
            diab_advice = ''

    st.success(diab_diagnosis)
    st.markdown(diab_advice)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.markdown("## ❤️ Heart Disease Prediction")
    st.markdown("Provide your health metrics below to assess heart disease risk.")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = safe_float_input(st.text_input('Age?'))
    with col2:
        sex = safe_float_input(st.text_input('Sex?'))
    with col3:
        cp = safe_float_input(st.text_input('Chest Pain types?'))
    with col1:
        trestbps = safe_float_input(st.text_input('Resting Blood Pressure?'))
    with col2:
        chol = safe_float_input(st.text_input('Serum Cholestoral in mg/dl?'))
    with col3:
        fbs = safe_float_input(st.text_input('Fasting Blood Sugar > 120 mg/dl?'))
    with col1:
        restecg = safe_float_input(st.text_input('Resting Electrocardiographic results?'))
    with col2:
        thalach = safe_float_input(st.text_input('Maximum Heart Rate achieved?'))
    with col3:
        exang = safe_float_input(st.text_input('Exercise Induced Angina?'))
    with col1:
        oldpeak = safe_float_input(st.text_input('ST depression induced by exercise relative to rest?'))
    with col2:
        slope = safe_float_input(st.text_input('Slope of the peak exercise ST segment?'))
    with col3:
        ca = safe_float_input(st.text_input('Major vessels colored by flourosopy?'))
    with col1:
        thal = safe_float_input(st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect'))

    heart_diagnosis = ''
    heart_advice =''

    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease :('
                heart_advice = """
    **Advice-:**
    - Consult a cardiologist regularly.
    - Take prescribed heart medications on time.
    - Maintain a heart-healthy diet (low salt, low fat).
    - Engage in light-to-moderate physical activity daily.
    - Avoid smoking and limit alcohol.
    - Monitor blood pressure, cholesterol, and sugar levels.
    - Manage stress through meditation and proper sleep.
    """
            else:
                heart_diagnosis = 'The person does not have heart disease :)'
                heart_advice = """
    ***Tips - Keep your heart healthy! ❤️***
    - Eat fresh fruits, vegetables, and whole grains.
    - Exercise regularly (walk, jog, swim).
    - Monitor blood pressure and cholesterol occasionally.
    - Avoid processed foods and trans fats.
    - Reduce stress and stay socially active.
    - Stay hydrated and sleep well.
    """
        except Exception as e:
            heart_diagnosis = f"Error in prediction: {str(e)}"

    st.success(heart_diagnosis)
    st.markdown(heart_advice)

# Parkinson's Prediction
if selected == 'Parkinsons Prediction':
    st.markdown("## 🧠 Parkinson's Disease Prediction")
    st.markdown("Enter voice-related metrics to assess risk of Parkinson's.")

    col1, col2, col3 = st.columns(3)
    with col1:
        fo = safe_float_input(st.text_input('MDVP:Fo(Hz)'))
    with col2:
        fhi = safe_float_input(st.text_input('MDVP:Fhi(Hz)'))
    with col3:
        flo = safe_float_input(st.text_input('MDVP:Flo(Hz)'))
    with col1:
        jitter_percent = safe_float_input(st.text_input('Jitter(%)'))
    with col2:
        jitter_abs = safe_float_input(st.text_input('Jitter(Abs)'))
    with col3:
        rap = safe_float_input(st.text_input('MDVP:RAP'))
    with col1:
        ppq = safe_float_input(st.text_input('MDVP:PPQ'))
    with col2:
        ddp = safe_float_input(st.text_input('Jitter:DDP'))
    with col3:
        shimmer = safe_float_input(st.text_input('Shimmer'))
    with col1:
        shimmer_db = safe_float_input(st.text_input('Shimmer(dB)'))
    with col2:
        apq3 = safe_float_input(st.text_input('APQ3'))
    with col3:
        apq5 = safe_float_input(st.text_input('APQ5'))
    with col1:
        apq = safe_float_input(st.text_input('APQ'))
    with col2:
        dda = safe_float_input(st.text_input('DDA'))
    with col3:
        nhr = safe_float_input(st.text_input('NHR'))
    with col1:
        hnr = safe_float_input(st.text_input('HNR'))

    

    parkinsons_diagnosis = ''
    parkinsons_advice= ''

    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr]])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease :("
                parkinsons_advice = """
    **Advice-:**
    - Consult a neurologist for proper medication and treatment.
    - Engage in physiotherapy and speech therapy.
    - Maintain a balanced diet and hydration.
    - Incorporate daily activities that enhance mobility and coordination.
    - Join support groups or mental wellness programs.
    - Take medications as prescribed and on time.
    - Monitor and report changes in symptoms.
    """
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease :)"
                parkinsons_advice = """
    ***Tips - Stay healthy and sharp!🧠***
    - Eat brain-boosting foods (omega-3 rich, antioxidant-rich).
    - Exercise your body and brain regularly.
    - Avoid excessive caffeine and smoking.
    - Stay socially engaged and mentally stimulated.
    - Prioritize good sleep hygiene.
    - Visit a neurologist if you ever notice tremors or changes in voice/movement.
    """
        except Exception as e:
            parkinsons_diagnosis = f"Error in prediction: {str(e)}"

    st.success(parkinsons_diagnosis)
    st.markdown(parkinsons_advice)

