import streamlit as st

def run():
    st.title("📊 Statistical Test Selector")

    selected_test = st.selectbox(
        "Select the type of statistical test you want to perform:",
        [
            "Z-Test (One Proportion)",
            "Z-Test (Two Population Means)",
            "T-Test (Equal Variances)",
            "T-Test (Unequal Variances)",
            "Two-Proportion Z-Test",
            "Confidence Intervals",
            "Normal Distribution Tools",
            "Sampling Distribution Tools",
            "Binomial Distribution",
            "Poisson Distribution",
            "Conditional Probability",
            "Bayes Theorem",
            "Combinatorics and Sample Spaces",
            "Classical Probability"
        ]
    )

    if selected_test == "Z-Test (One Proportion)":
        import modules.one_prop_z_test as one_prop
        one_prop.run()

    elif selected_test == "Z-Test (Two Population Means)":
        import modules.z_test_two_means as z
        z.run()

    elif selected_test == "T-Test (Equal Variances)":
        import modules.t_test_equal_var as t_equal
        t_equal.run()

    elif selected_test == "T-Test (Unequal Variances)":
        import modules.t_test_unequal_var as t_unequal
        t_unequal.run()

    elif selected_test == "Two-Proportion Z-Test":
        import modules.two_prop_z_test as two_prop
        two_prop.run()

    elif selected_test == "Confidence Intervals":
        import modules.confidence_intervals as ci
        ci.run()
    
    elif selected_test == "Normal Distribution Tools":
        import modules.normal_distribution_tools as nd
        nd.run()
    
    elif selected_test == "Sampling Distribution Tools":
        import modules.sampling_distribution_tools as sdt
        sdt.run()
   
    elif selected_test == "Binomial Distribution":
        import modules.binomial_distribution as bd
        bd.run()

    elif selected_test == "Poisson Distribution":
        import modules.poisson_distribution as pd
        pd.run()

    elif selected_test == "Conditional Probability":
        import modules.conditional_probability as cp
        cp.run()

    elif selected_test == "Bayes Theorem":
        import modules.bayes_theorem as bt
        bt.run()

    elif selected_test == "Combinatorics and Sample Spaces":
        import modules.combinatorics as cb
        cb.run()

    elif selected_test == "Classical Probability":
        import modules.classical_probability as clp
        clp.run()
