import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy import stats
import pandas as pd
import io
from fpdf import FPDF
import tempfile

def run_descriptive_analysis(series, column_name):
    if len(series.dropna()) < 2:
        st.error("❌ Not enough data to compute descriptive statistics. At least 2 values are required.")
        return

    st.write("### 📊 Summary Statistics")
    desc = {
        'Count': series.count(),
        'Mean': series.mean(),
        'Median': series.median(),
        'Mode': series.mode().values.tolist(),
        'Min': series.min(),
        'Max': series.max(),
        'Range': series.max() - series.min(),
        'Variance': series.var(),
        'Standard Deviation': series.std(),
        'Q1': series.quantile(0.25),
        'Q2 (Median)': series.quantile(0.50),
        'Q3': series.quantile(0.75),
        'IQR': series.quantile(0.75) - series.quantile(0.25)
    }

    for key, value in desc.items():
        st.write(f"**{key}:** {value}")

    q1 = desc['Q1']
    q3 = desc['Q3']
    iqr = desc['IQR']
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = series[(series < lower_bound) | (series > upper_bound)]
    st.write(f"**Outliers detected ({len(outliers)}):** {outliers.values}")

    # 📈 Visualizaciones
    st.write("### 📈 Visualizations")
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    sns.histplot(series, kde=True, bins=20, ax=axs[0])
    axs[0].set_title(f"Histogram of {column_name}")

    sns.boxplot(x=series, ax=axs[1])
    axs[1].set_title(f"Boxplot of {column_name}")

    freq = series.value_counts().nlargest(10)
    sns.barplot(x=freq.index, y=freq.values, ax=axs[2])
    axs[2].set_title(f"Top 10 Frequencies of {column_name}")
    axs[2].tick_params(axis='x', rotation=45)

    # Guardar gráfico como imagen temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
        fig.savefig(tmpfile.name, bbox_inches='tight')
        img_path = tmpfile.name
    st.pyplot(fig, use_container_width=True)

    # 📤 Exportación de resultados como PDF 
    st.write("### 📤 Export Report as PDF")

    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", 'B', 14)
            self.cell(0, 10, f"Descriptive Analysis Report for: {column_name}", ln=True, align='C')
            self.ln(10)

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    for key, value in desc.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Outliers detected ({len(outliers)}): {outliers.values.tolist()}")
    pdf.ln(10)

    pdf.image(img_path, x=10, w=190)

    pdf_output = io.BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    pdf_output.write(pdf_bytes)
    pdf_output.seek(0)

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf_output,
        file_name=f"{column_name}_report.pdf",
        mime="application/pdf"
    )

