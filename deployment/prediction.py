import pandas as pd
import streamlit as st
import numpy as np
import pickle
import json

# Load Model

# Modelling
with open('cat_model.pkl', 'rb') as file_1:
    cat_model = pickle.load(file_1)

with open('cat_process.pkl', 'rb') as file_2:
    cat_process = pickle.load(file_2)

# Pre-processing
with open('fe_pipeline.pkl', 'rb') as file_3:
    fe_pipeline = pickle.load(file_3)
    
# List Numeric & Category
with open('num_cols_sc.txt', 'r') as file_4:
    num_cols_sc = json.load(file_4)
    
with open('num_cols_nsc.txt', 'r') as file_5:
    num_cols_nsc = json.load(file_5)
    
def run():
    # Membuat Form
    with st.form(key = 'milk_quality'):
        pH = st.slider('pH', min_value= 2.5, max_value=10.0, value=4.0)
        Temperature = st.slider('Temperature', min_value=30, max_value=100, value=60)
        Taste = st.selectbox('Taste of Milk', (0, 1), help= '0 is Bad, 1 is Good')
        Odor = st.selectbox('Odor of Milk', (0, 1), help= '0 is Bad, 1 is Good')
        Fat = st.selectbox('Fat of Milk', (0, 1), help= '0 is Low, 1 is High')
        Turbidity = st.selectbox('Turbidity of Milk', (0, 1), help= '0 is Low, 1 is High')
        Colour = st.slider('Colour', min_value=240, max_value=255, value=250)
        
        submitted = st.form_submit_button('Predict')

    # Data Inference
    data_inf = {
        'pH' : pH,
        'Temperature' : Temperature,
        'Taste' : Taste,
        'Odor' : Odor,
        'Fat' : Fat,
        'Turbidity' : Turbidity,
        'Colour' : Colour
    }
    
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)
    
    if submitted:
        # Feature Engineering & Modelling
        y_pred_inf = cat_process.predict(data_inf)
        
        st.write('# Milks Grade :', str(int(y_pred_inf)))

if __name__ == '__main__':
    run()