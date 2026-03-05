import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
diseases = ["DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO"]
st.title("Question 4: Disease vs ICU Admission")
icu_data = {}
for disease in diseases:
    icu_cases = df[(df[disease] == 1) & (df["ICU"] == 1)].shape[0]
    icu_data[disease] = icu_cases
icu_df = pd.DataFrame.from_dict(icu_data, orient="index", columns=["ICU Cases"])

selected_diseases = st.multiselect(
    "Select one or more diseases",
    diseases,
    default=["DIABETES","HYPERTENSION","CARDIOVASCULAR"]
)

if selected_diseases:
    filtered_df = icu_df.loc[selected_diseases]
    st.bar_chart(filtered_df)
