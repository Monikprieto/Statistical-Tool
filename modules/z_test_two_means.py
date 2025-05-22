
import streamlit as st
from scipy.stats import norm
import numpy as np

def run():
    st.header("📈 Z-Test for Two Population Means")

    st.markdown("Use this test when both population standard deviations are known.")

    with st.form("z_test_form"):
        st.subheader("Enter Sample Data")

        mean1 = st.number_input("Sample 1 Mean (x̄₁)", value=0.0)
        std_dev1 = st.number_input("Population Std Dev for Sample 1 (σ₁)", value=1.0)
        n1 = st.number_input("Sample 1 Size (n₁)", min_value=1, step=1, value=30)

        mean2 = st.number_input("Sample 2 Mean (x̄₂)", value=0.0)
        std_dev2 = st.number_input("Population Std Dev for Sample 2 (σ₂)", value=1.0)
        n2 = st.number_input("Sample 2 Size (n₂)", min_value=1, step=1, value=30)

        alpha = st.number_input("Significance Level (α)", min_value=0.01, max_value=0.10, step=0.01, value=0.05)

        alternative = st.selectbox(
            "Alternative Hypothesis (H₁)",
            ["μ₁ ≠ μ₂ (Two-tailed)", "μ₁ > μ₂ (Right-tailed)", "μ₁ < μ₂ (Left-tailed)"]
        )

        submitted = st.form_submit_button("Run Z-Test")

    if submitted:
        pooled_se = np.sqrt((std_dev1**2 / n1) + (std_dev2**2 / n2))
        z_score = (mean1 - mean2) / pooled_se

        if alternative == "μ₁ ≠ μ₂ (Two-tailed)":
            p_value = 2 * (1 - norm.cdf(abs(z_score)))
        elif alternative == "μ₁ > μ₂ (Right-tailed)":
            p_value = 1 - norm.cdf(z_score)
        else:
            p_value = norm.cdf(z_score)

        st.subheader("🧾 Results")
        st.write(f"Z-Score: **{z_score:.4f}**")
        st.write(f"P-Value: **{p_value:.4f}**")

        st.markdown("### 📌 Test Decision Based on P-Value")
        st.table({
            "Significance Level (α)": [alpha],
            "P-Value": [round(p_value, 4)],
            "Decision": ["Reject H₀ ✅" if p_value < alpha else "Do not reject H₀ ❌"]
        })
