import streamlit as st
import ast

def run():
    st.header("🎲 Classical Probability Calculator")

    st.markdown("This tool allows you to calculate classical probabilities using your own sample space and a condition.")
    st.markdown("### Step 1: Define the sample space")
    st.markdown("Enter your space as a list. Example:")
    st.code("['♠', '♥', '♦', '♣']", language="python")
    st.code("[(1,1), (1,2), ..., (6,6)]", language="python")

    sample_space_input = st.text_area("Sample Space", value="[(i, j) for i in range(1, 7) for j in range(1, 7)]")

    try:
        sample_space = eval(sample_space_input)
        if isinstance(sample_space, list) and len(sample_space) > 0:
            st.success(f"Sample space has {len(sample_space)} outcomes.")
        else:
            st.error("Sample space must be a non-empty list.")
            return
    except Exception as e:
        st.error(f"Invalid sample space: {e}")
        return

    st.markdown("### Step 2: Define the event condition")
    st.code("Use 'x' as the variable. Example: sum(x) == 8")
    condition = st.text_input("Condition", value="sum(x) == 8")

    try:
        favorable_set = {x for x in sample_space if eval(condition)}
    except Exception as e:
        st.error(f"Invalid condition: {e}")
        return

    total_outcomes = len(sample_space)
    favorable_count = len(favorable_set)
    probability = favorable_count / total_outcomes if total_outcomes else 0

    st.markdown("### 📊 Results")
    st.write(f"Total outcomes: **{total_outcomes}**")
    st.write(f"Favorable outcomes: **{favorable_count}**")
    st.write(f"Classical Probability: **{favorable_count}/{total_outcomes} = {probability:.4f}**")

    if favorable_count > 0:
        st.markdown("### ✅ Favorable Outcomes:")
        st.text(", ".join(str(x) for x in sorted(favorable_set)))
