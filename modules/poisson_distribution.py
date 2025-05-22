import streamlit as st
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.header("🔢 Poisson Distribution Calculator")

    st.markdown("Use this module to compute probabilities and visualize the Poisson distribution.")

    lam = st.number_input("Average Rate (λ)", min_value=0.01, value=4.0)
    x = st.number_input("Target Value (x)", min_value=0, step=1, value=2)

    calc_type = st.radio("Select Probability Type", [
        "P(X = x)",
        "P(X ≤ x)",
        "P(X ≥ x)"
    ])

    if calc_type == "P(X = x)":
        prob = poisson.pmf(x, lam)
    elif calc_type == "P(X ≤ x)":
        prob = poisson.cdf(x, lam)
    else:
        prob = 1 - poisson.cdf(x - 1, lam)

    st.markdown("### 📊 Result")
    st.write(f"**{calc_type} = {prob:.4f}**")

    st.markdown("### 📈 Poisson Distribution Plot")
    x_vals = np.arange(0, int(lam + 4 * np.sqrt(lam)) + 1)
    y_vals = poisson.pmf(x_vals, lam)

    fig, ax = plt.subplots(figsize=(15, 5))
    bars = ax.bar(x_vals, y_vals, color="lightblue", edgecolor="black")
    if 0 <= x < len(bars):
        bars[int(x)].set_color("orange")

    ax.set_title(f"Poisson Distribution (λ = {lam})")
    ax.set_xlabel("Number of Events")
    ax.set_ylabel("Probability")
    st.pyplot(fig)
