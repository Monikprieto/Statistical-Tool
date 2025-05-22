import streamlit as st

def run():
    st.header("🧠 Bayes' Theorem Calculator")

    st.markdown("Use this tool to compute probabilities using **Bayes' Theorem**.")
    st.latex(r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}")

    st.markdown("Bayes' Theorem is particularly useful for interpreting diagnostic tests, risk analysis, and more.")

    p_a = st.number_input("P(A) — Prior probability of A (e.g., disease prevalence)", min_value=0.0, max_value=1.0, value=0.01)
    p_b_given_a = st.number_input("P(B|A) — Sensitivity (True Positive Rate)", min_value=0.0, max_value=1.0, value=0.99)
    p_b_given_not_a = st.number_input("P(B|¬A) — False Positive Rate", min_value=0.0, max_value=1.0, value=0.05)

    p_not_a = 1 - p_a
    p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a

    if p_b > 0:
        p_a_given_b = (p_b_given_a * p_a) / p_b
        st.markdown("### 📊 Result")
        st.write(f"P(A|B) — Posterior probability = **{p_a_given_b:.4f}**")
    else:
        st.error("P(B) is zero. Cannot compute posterior probability.")

    st.markdown("---")
    st.markdown("### 🧾 Interpretation")
    st.markdown("- This value represents the **updated probability of A** given that B has occurred.")
    st.markdown("- Common use cases include disease detection (A = has disease, B = positive test).")
