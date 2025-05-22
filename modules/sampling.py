
import numpy as np
import streamlit as st
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import io
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def run_sampling_analysis(series, confidence_level):
    st.write("### 📊 Sampling Statistics")

    if confidence_level < 50 or confidence_level >= 100:
        st.error("Please enter a confidence level between 50 and 99.9")
        return

    n = len(series)
    sample_mean = np.mean(series)
    sample_std = np.std(series, ddof=1)
    cv = (sample_std / sample_mean) * 100 
    se = sample_std / np.sqrt(n)

    alpha = 1 - (confidence_level / 100)
    z_score = stats.norm.ppf(1 - alpha / 2)
    margin_error = z_score * se

    ci_lower = sample_mean - margin_error
    ci_upper = sample_mean + margin_error

    ucl = sample_mean + 3 * se
    lcl = sample_mean - 3 * se

    st.write(f"**Sample Size (n):** {n}")
    st.write(f"**Sample Mean (x̄):** {sample_mean:.4f}")
    st.write(f"**Sample Std Dev (s):** {sample_std:.4f}")
    st.write(f"**Standard Error (SE):** {se:.4f}")
    st.write(f"**Z-critical ({confidence_level}%):** {z_score:.4f}")
    st.write(f"**Margin of Error:** ±{margin_error:.4f}")
    st.write(f"**{confidence_level}% Confidence Interval:** ({ci_lower:.4f}, {ci_upper:.4f})")
    st.write(f"**Coefficient of Variation (CV):** {cv:.2f}%")
    st.write(f"**Upper Control Limit (UCL):** {ucl:.4f}")
    st.write(f"**Lower Control Limit (LCL):** {lcl:.4f}")

    st.write("\n### 📈 Visualizations")
    fig, axs = plt.subplots(1, 3, figsize=(20, 5))

    sns.histplot(series, kde=True, bins=20, ax=axs[0], color='skyblue')
    axs[0].set_title("Sample Distribution")
    axs[0].set_xlabel("Values")
    axs[0].set_ylabel("Frequency")

    axs[1].errorbar(x=0, y=sample_mean, yerr=margin_error, fmt='o', capsize=10, color='green')
    axs[1].set_xlim(-1, 1)
    axs[1].set_ylim(series.min() - se, series.max() + se)
    axs[1].set_title("Confidence Interval")
    axs[1].set_xticks([])
    axs[1].set_ylabel("Value")

    axs[2].plot(series.index, series.values, marker='o', linestyle='-', color='black')
    axs[2].axhline(ucl, color='red', linestyle='--', label='UCL')
    axs[2].axhline(sample_mean, color='blue', linestyle='-', label='Mean')
    axs[2].axhline(lcl, color='red', linestyle='--', label='LCL')
    axs[2].set_title("Control Limits")
    axs[2].set_xlabel("Sample Index")
    axs[2].set_ylabel("Value")
    axs[2].legend()

    plt.tight_layout()
    st.pyplot(fig)

    # Exportación con ReportLab
    st.write("### 📤 Export Report as PDF")

    # Generar PDF al vuelo
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)

    y = 750
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "📊 Sampling Report")

    y -= 25  # bajar antes de comenzar con el contenido

    c.setFont("Helvetica", 10)
    line_spacing = 18

    report_values = [
        ("Sample Size (n):", n),
        ("Sample Mean (x̄):", f"{sample_mean:.4f}"),
        ("Sample Std Dev (s):", f"{sample_std:.4f}"),
        ("Standard Error (SE):", f"{se:.4f}"),
        (f"Z-critical ({confidence_level}%):", f"{z_score:.4f}"),
        ("Margin of Error:", f"±{margin_error:.4f}"),
        (f"{confidence_level}% Confidence Interval:", f"({ci_lower:.4f}, {ci_upper:.4f})"),
        ("Coefficient of Variation (CV):", f"{cv:.2f}%"),
        ("Upper Control Limit (UCL):", f"{ucl:.4f}"),
        ("Lower Control Limit (LCL):", f"{lcl:.4f}")
    ]

    for label, value in report_values:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, label)
        c.setFont("Helvetica", 10)
        c.drawString(200, y, str(value))
        y -= line_spacing

    # Calcular posición segura para el gráfico
    graphic_y = y - 20
    if graphic_y < 250:
        graphic_y = 250

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        fig.savefig(tmpfile.name, bbox_inches="tight")
        img_path = tmpfile.name

    c.drawImage(img_path, 50, 350, width=500, height=200, preserveAspectRatio=True, mask="auto")
    c.save()

    pdf_buffer.seek(0)

    # Mostrar botón funcional
    st.download_button(
        label="📄 Download PDF Report",
        data=pdf_buffer.getvalue(),
        file_name="sampling_report.pdf",
        mime="application/pdf"
    )
