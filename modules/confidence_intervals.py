import streamlit as st
from scipy.stats import norm, t
import numpy as np

def run():
    st.header("📏 Confidence Interval Calculator")

    st.markdown("Choose the type of confidence interval to calculate:")
    ic_type = st.radio("Interval Type", [
        "Mean (σ known)",
        "Mean (σ unknown)",
        "Proportion"
    ])

    if ic_type == "Mean (σ known)":
        st.subheader("For the Mean (σ known)")
        x_bar = st.number_input("Sample Mean (x̄)", value=42.5)
        sigma = st.number_input("Population Std Dev (σ)", min_value=0.0001, value=5.0)
        n = st.number_input("Sample Size (n)", min_value=1, value=35)
        conf_level = st.slider("Confidence Level", 0.80, 0.99, 0.90)

        alpha = 1 - conf_level
        z_crit = norm.ppf(1 - alpha / 2)
        se = sigma / np.sqrt(n)
        me = z_crit * se
        lower, upper = x_bar - me, x_bar + me

        st.markdown("### 📊 Results")
        st.write(f"Z-Critical Value: **{z_crit:.3f}**")
        st.write(f"Standard Error: **{se:.4f}**")
        st.write(f"Margin of Error: **{me:.4f}**")
        st.write(f"**Confidence Interval:** ({lower:.4f}, {upper:.4f})")

    elif ic_type == "Mean (σ unknown)":
        st.subheader("For the Mean (σ unknown)")
        x_bar = st.number_input("Sample Mean (x̄)", value=45.0)
        s = st.number_input("Sample Std Dev (s)", min_value=0.0001, value=5.0)
        n = st.number_input("Sample Size (n)", min_value=2, value=15)
        conf_level = st.slider("Confidence Level", 0.80, 0.99, 0.95)

        alpha = 1 - conf_level
        df = n - 1
        t_crit = t.ppf(1 - alpha / 2, df)
        se = s / np.sqrt(n)
        me = t_crit * se
        lower, upper = x_bar - me, x_bar + me

        st.markdown("### 📊 Results")
        st.write(f"Degrees of Freedom: **{df}**")
        st.write(f"T-Critical Value: **{t_crit:.3f}**")
        st.write(f"Standard Error: **{se:.4f}**")
        st.write(f"Margin of Error: **{me:.4f}**")
        st.write(f"**Confidence Interval:** ({lower:.4f}, {upper:.4f})")

    else:
        st.subheader("For Proportions")
        x = st.number_input("Number of Successes (x)", min_value=0, value=176)
        n = st.number_input("Sample Size (n)", min_value=1, value=225)
        conf_level = st.slider("Confidence Level", 0.80, 0.99, 0.95)

        alpha = 1 - conf_level
        p_hat = x / n
        z_crit = norm.ppf(1 - alpha / 2)
        se = np.sqrt(p_hat * (1 - p_hat) / n)
        me = z_crit * se
        lower, upper = p_hat - me, p_hat + me

        st.markdown("### 📊 Results")
        st.write(f"Sample Proportion (p̂): **{p_hat:.4f}**")
        st.write(f"Z-Critical Value: **{z_crit:.3f}**")
        st.write(f"Standard Error: **{se:.4f}**")
        st.write(f"Margin of Error: **{me:.4f}**")
        st.write(f"**Confidence Interval:** ({lower:.4f}, {upper:.4f})")
