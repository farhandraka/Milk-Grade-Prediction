import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Choose Page :', ('Exploratory Data Analysis', 'Prediction Milks Grade'))

if navigation == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()