import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def run_encoding_tool(df):
    st.header("📘 Categorical Encoding")

    cat_cols = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    if not cat_cols:
        st.warning("⚠️ No categorical columns found in the dataset.")
        return

    selected_cols = st.multiselect("🔠 Select categorical columns to encode:", cat_cols)
    method = st.radio("🛠️ Select encoding method:", ["One-Hot Encoding", "Label Encoding"])

    if st.button("⚙️ Apply Encoding") and selected_cols:
        df_encoded = df.copy()

        if method == "One-Hot Encoding":
            df_encoded = pd.get_dummies(df_encoded, columns=selected_cols)
        else:
            label_encoders = {}
            for col in selected_cols:
                le = LabelEncoder()
                df_encoded[col] = le.fit_transform(df_encoded[col])
                label_encoders[col] = le

        st.success("✅ Encoding applied successfully!")

        st.subheader("🔍 Encoded Dataset Preview")
        st.dataframe(df_encoded.head())

        csv = df_encoded.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Encoded CSV", data=csv, file_name="encoded_data.csv", mime="text/csv")

    elif selected_cols:
        st.info("⚠️ Press the button above to apply encoding.")
