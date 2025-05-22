import streamlit as st
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def plot_distribution(z_score, tail="less"):
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x)

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(x, y, label="Standard Normal Distribution")

    if tail == "less":
        ax.fill_between(x, 0, y, where=(x <= z_score), color="skyblue", alpha=0.5)
    elif tail == "greater":
        ax.fill_between(x, 0, y, where=(x > z_score), color="skyblue", alpha=0.5)
    elif tail == "between":
        ax.fill_between(x, 0, y, where=(x > z_score[0]) & (x < z_score[1]), color="skyblue", alpha=0.5)

    ax.axvline(x=z_score if isinstance(z_score, float) else z_score[0], color='red', linestyle='--')
    if isinstance(z_score, tuple):
        ax.axvline(x=z_score[1], color='red', linestyle='--')

    ax.set_title("Standard Normal Distribution")
    st.pyplot(fig)

def run():
    st.header("📦 Sampling Distribution Tools")

    mode = st.radio("Select Type of Distribution", [
        "Central Limit Theorem (Mean)",
        "Sampling Distribution of Proportion"
    ])

    if mode == "Central Limit Theorem (Mean)":
        st.subheader("📐 Central Limit Theorem")

        mu = st.number_input("Population Mean (μ)", value=7.0)
        sigma = st.number_input("Population Std Dev (σ)", min_value=0.0001, value=3.0)
        n = st.number_input("Sample Size (n)", min_value=1, value=100)
        x = st.number_input("Sample Mean (x̄)", value=8.0)
        direction = st.radio("Probability Direction", ["P(X ≤ x)", "P(X > x)"])

        se = sigma / np.sqrt(n)
        z = (x - mu) / se
        p = norm.cdf(z) if direction == "P(X ≤ x)" else 1 - norm.cdf(z)

        st.markdown("### 🧾 Results")
        st.write(f"Standard Error (SE): **{se:.4f}**")
        st.write(f"Z-Score: **{z:.4f}**")
        st.write(f"Probability {direction}: **{p:.4f}**")

        plot_distribution(z, "less" if direction == "P(X ≤ x)" else "greater")

    elif mode == "Sampling Distribution of Proportion":
        st.subheader("📊 Sampling Distribution of Proportion")

        x = st.number_input("Number of Successes (x)", min_value=0, value=45)
        n = st.number_input("Sample Size (n)", min_value=1, value=150)
        P = st.number_input("Population Proportion (P)", min_value=0.0, max_value=1.0, value=0.3)
        tail_type = st.radio("Probability Direction", ["P(x̂ ≤ x)", "P(x̂ > x)", "P(a < x̂ < b)"])

        p_hat = x / n
        q = 1 - P
        se = np.sqrt(P * q / n)
        z = (p_hat - P) / se

        np_check = n * P
        nq_check = n * (1 - P)
        normal_ok = np_check >= 5 and nq_check >= 5

        st.markdown("### 🧾 Results")
        st.write(f"Sample Proportion (p̂): **{p_hat:.4f}**")
        st.write(f"Standard Error: **{se:.4f}**")
        st.write(f"Z-Score: **{z:.4f}**")
        st.write(f"Conditions: nP = {np_check:.2f}, n(1-P) = {nq_check:.2f} → {'✅ Normal Approx OK' if normal_ok else '❌ Use Binomial'}")

        if tail_type == "P(x̂ ≤ x)":
            p = norm.cdf(z) if normal_ok else np.nan
            st.write(f"Probability: **{p:.4f}**")
            if normal_ok:
                plot_distribution(z, "less")

        elif tail_type == "P(x̂ > x)":
            p = 1 - norm.cdf(z) if normal_ok else np.nan
            st.write(f"Probability: **{p:.4f}**")
            if normal_ok:
                plot_distribution(z, "greater")

        else:
            a = st.number_input("Lower Bound (a)", min_value=0.0, max_value=1.0, value=0.4)
            b = st.number_input("Upper Bound (b)", min_value=0.0, max_value=1.0, value=0.4667)
            za = (a - P) / se
            zb = (b - P) / se
            p = norm.cdf(zb) - norm.cdf(za) if normal_ok else np.nan
            st.write(f"Z-scores: a = {za:.4f}, b = {zb:.4f}")
            st.write(f"Probability between a and b: **{p:.4f}**")
            if normal_ok:
                plot_distribution((za, zb), "between")
