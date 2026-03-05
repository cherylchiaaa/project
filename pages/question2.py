import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
st.title("Question 2: Distribution of COVID-19 Cases by Sex and Age Group")
bins = [0,10,20,30,40,50,60,70,80,90,100]
labels = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
df["age_group"] = pd.cut(df["AGE"], bins=bins, labels=labels)
gender_age = df.groupby(["age_group","SEX"]).size().unstack()
show_nonzero = st.checkbox("Show only age groups with cases", value=True)

if show_nonzero:
    gender_age_filtered = gender_age[(gender_age.T != 0).any()]
else:
    gender_age_filtered = gender_age

st.bar_chart(gender_age_filtered)