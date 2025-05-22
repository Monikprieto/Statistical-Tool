import pandas as pd
from scipy.stats import chi2_contingency, chi2
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({
    'font.size': 8
})

def run_chi_square_test():
    st.title("Chi-Square Test of Independence")
    st.write("This test checks whether two categorical variables are independent by comparing observed and expected frequencies.")

    if "uploaded_file" not in st.session_state or st.session_state["uploaded_file"] is None:
        st.warning("📂 Please upload a valid contingency table CSV file from the sidebar to run this analysis.")
        return

    try:
        chi_data = st.session_state["uploaded_file"]

        st.subheader("Contingency Table (Observed Frequencies)")
        st.dataframe(chi_data)

        # Convertir todos los valores a numéricos si es posible
        chi_data = chi_data.set_index(chi_data.columns[0])
        chi_data_numeric = chi_data.apply(pd.to_numeric, errors='coerce')

        if chi_data_numeric.isnull().values.any():
            st.error("❌ The contingency table contains non-numeric values. Please check your CSV.")
            return

        if (chi_data_numeric < 0).any().any():
            st.error("Contingency table should only contain non-negative values.")
            return

        # Selección de nivel de significancia fuera del botón
        alpha = st.slider("Select significance level (α)", 0.01, 0.10, 0.05, step=0.01)

        # Ejecutar análisis solo si se presiona el botón
        if st.button("Run Chi-Square Test"):
            chi2_val, p, dof, expected = chi2_contingency(chi_data_numeric)
            critical_val = chi2.ppf(1 - alpha, df=dof) 

            st.write(f"**Chi-Square Statistic:** {chi2_val:.4f}")
            st.write(f"**Degrees of Freedom:** {dof}")
            st.write(f"**Significance Level (α):** {alpha}")
            st.write(f"**Critical Value (χ²):** {critical_val:.4f}")
            st.write(f"**P-Value:** {p:.4f}")

            if p < alpha:
                st.success("✅ The result is significant. Reject the null hypothesis.")
            else:
                st.info("ℹ️ No significant association found. Fail to reject the null hypothesis.")
            
            st.subheader("Expected Frequencies")
            expected_df = pd.DataFrame(expected, index=chi_data.index, columns=chi_data.columns)
            st.dataframe(expected_df)

                       
            # Crear dos columnas
            col1, col2 = st.columns(2)
            
            with col1:
                # 📈 Observed Frequencies (Bar Chart)
                st.subheader("📈 Observed Frequencies (Bar Chart)")
                fig_obs, ax_obs = plt.subplots(figsize=(3, 2), dpi=100)
                chi_data.plot(kind='bar', ax=ax_obs, legend=True)
                ax_obs.set_ylabel("Count", fontsize=5)
                ax_obs.set_xlabel("Player", fontsize=5)
                ax_obs.set_title("Observed Frequencies", fontsize=7)
                ax_obs.legend(fontsize=6)
                ax_obs.tick_params(axis='x', labelsize=6)  
                ax_obs.tick_params(axis='y', labelsize=6)  
                st.pyplot(fig_obs, use_container_width=False)

            # 📈 Expected Frequencies (Bar Chart)
            with col2:
                st.subheader("📈 Expected Frequencies (Bar Chart)")
                fig_exp, ax_exp = plt.subplots(figsize=(3, 2), dpi=100)
                expected_df.plot(kind='bar', ax=ax_exp, legend=True)
                ax_exp.set_ylabel("Count", fontsize=5)
                ax_exp.set_xlabel("Player", fontsize=5)
                ax_exp.set_title("Expected Frequencies", fontsize=7)
                ax_exp.legend(fontsize=6)
                ax_exp.tick_params(axis='x', labelsize=6)
                ax_exp.tick_params(axis='y', labelsize=6)
                st.pyplot(fig_exp, use_container_width=False)

            # 🔥 Heatmap of Observed - Expected
            st.subheader("🔥 Heatmap of Observed - Expected")
            diff = chi_data - expected_df
            fig_diff, ax_diff = plt.subplots(figsize=(3, 2), dpi=100)
            sns.heatmap(diff, annot=True, cmap="coolwarm", center=0, ax=ax_diff, annot_kws={"size": 5})
            ax_diff.set_title("Difference (Observed - Expected)", fontsize=7)
            ax_diff.tick_params(axis='x', labelsize=5)
            ax_diff.tick_params(axis='y', labelsize=5)
            
            # Ejes
            ax_diff.set_xticklabels(ax_diff.get_xticklabels(), fontsize=6)
            ax_diff.set_yticklabels(ax_diff.get_yticklabels(), fontsize=6)

            # Ajuste del tamaño de letra en la barra de colores
            cbar = ax_diff.collections[0].colorbar
            cbar.ax.tick_params(labelsize=6)

            st.pyplot(fig_diff, use_container_width=False)  

    except Exception as e:
        st.error(f"⚠️ Error processing the Chi-Square test: {e}")
