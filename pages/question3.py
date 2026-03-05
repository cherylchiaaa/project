import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
st.title("Question 3: Patients Who Required Intubation")
intubed_counts = df["INTUBATED"].value_counts()
labels = intubed_counts.index.map({1:"YES", 2:"NO", 97:"DOES NOT APPLY", 98:"IGNORED", 99:"UNKNOWN"})
# st.write(intubed_counts)
# st.bar_chart(intubed_counts)
fig, ax = plt.subplots()

ax.pie(
    intubed_counts,
    labels=labels,
    autopct="%1.1f%%",
    startangle=180
)

st.pyplot(fig)