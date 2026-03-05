# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("dataset.csv")
# st.title("Question 5: Diseases Among Deceased Patients")
# deceased = df[df["DATE_OF_DEATH"] != "9999-99-99"]
# diseases = ["DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO"]
# disease_counts = {}
# for disease in diseases:
#     disease_counts[disease] = (deceased[disease] == 1).sum()
# disease_df = pd.DataFrame.from_dict(disease_counts, orient="index", columns=["Cases"])
# st.line_chart(disease_df)
# /opt/anaconda3/bin/python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

# Load dataset
df = pd.read_csv("dataset.csv")

st.title("Question 5: Diseases Among Deceased Patients")

# Filter deceased
deceased = df[df["DATE_OF_DEATH"] != "9999-99-99"]

# Diseases list
diseases = ["DIABETES", "COPD", "ASTHMA", "INMUSUPR",
            "HYPERTENSION", "CARDIOVASCULAR",
            "OBESITY", "CHRONIC_KIDNEY", "TOBACCO"]

# Count diseases
disease_counts = {disease: (deceased[disease] == 1).sum() for disease in diseases}
disease_df = pd.DataFrame.from_dict(disease_counts, orient="index", columns=["Cases"])

# Show line chart
st.line_chart(disease_df)

# ---------------------------
# Generate PDF function
# ---------------------------
def generate_pdf(disease_df):
    pdf_buffer = io.BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Add logo if exists
    if os.path.exists("logo.png"):
        elements.append(Image("logo.png", width=120, height=45, hAlign='LEFT'))
        elements.append(Spacer(1, 15))

    # Title
    elements.append(Paragraph("Diseases Among Deceased Patients", styles["Heading1"]))
    elements.append(Spacer(1, 10))

    # Timestamp
    elements.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["Normal"]))
    elements.append(Spacer(1, 20))

    # Create Matplotlib chart for PDF
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(disease_df.index, disease_df["Cases"], marker='o')
    ax.set_title("Diseases Among Deceased Patients")
    ax.set_xlabel("Disease")
    ax.set_ylabel("Number of Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save chart to BytesIO
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    plt.close(fig)
    img_buffer.seek(0)

    # Add chart image to PDF
    elements.append(Image(img_buffer, width=450, height=250))

    # Build PDF
    doc.build(elements)
    pdf_buffer.seek(0)
    return pdf_buffer

# ---------------------------
# Download button
# ---------------------------
pdf_file = generate_pdf(disease_df)

st.download_button(
    label="📥 Download Chart as PDF",
    data=pdf_file,
    file_name="diseases_deceased_chart.pdf",
    mime="application/pdf"
)