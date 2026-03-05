import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Project",
    page_icon=":smiley:",
    layout="wide"
)

st.markdown('# Welcome to my Streamlit App! :wave:')

tab1, tab2 = st.tabs(["Intro", "Company"])

with tab1:
    st.write("Welcome to my Streamlit app! This app is designed to showcase various data visualizations and insights related to COVID-19. You can navigate through the tabs to explore different aspects of the data, including age groups, intubation rates, and ICU admissions. Feel free to interact with the charts and discover interesting trends in the dataset!")

with tab2:
    st.image("fa_logo.png", width=200)
