import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

st.title("Question 1: COVID-19 Cases by Age Group")
bins = [0,10,20,30,40,50,60,70,80,90,100]
labels = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
df["age_group"] = pd.cut(df["AGE"], bins=bins, labels=labels)
age_counts = df["age_group"].value_counts().sort_index()
age_range = st.slider(
    "Select Age Range",
    0, 100, (20,60)
)
filtered_df = df[(df["AGE"] >= age_range[0]) & (df["AGE"] <= age_range[1])]
filtered_age_counts = filtered_df["age_group"].value_counts().sort_index()
st.bar_chart(filtered_age_counts)
st.write("The age group that are most susceptible to COVID-19 is 40-50 years old.")

