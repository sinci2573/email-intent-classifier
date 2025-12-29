import sys
import os
import streamlit as st
import pandas as pd

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.llm_client import classify_email

# --------------------------------------------------
# App Title
# --------------------------------------------------
st.title("📧 Email Intent & Priority Classifier")
st.write("This app classifies customer emails into intent, priority, and sentiment.")

# --------------------------------------------------
# SECTION 1: Single Email Classification
# --------------------------------------------------
st.header("✉️ Single Email Classification")

subject = st.text_input("Email Subject")
body = st.text_area("Email Body")

if st.button("Classify"):
    if not subject or not body:
        st.warning("Please enter both subject and body.")
    else:
        result = classify_email(subject, body)

        st.subheader("🧠 Classification Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Intent", result["intent"])
        with col2:
            st.metric("Priority", result["priority"])
        with col3:
            st.metric("Sentiment", result["sentiment"])

# --------------------------------------------------
# SECTION 2: Batch Email Classification (CSV Upload)
# --------------------------------------------------
st.divider()
st.header("📂 Batch Email Classification (CSV Upload)")

st.write("Upload a CSV file with **subject** and **body** columns.")

uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        required_columns = {"subject", "body"}
        if not required_columns.issubset(df.columns):
            st.error("CSV must contain 'subject' and 'body' columns.")
        else:
            st.subheader("📄 Uploaded Data Preview")
            st.dataframe(df.head())

            if st.button("🚀 Classify CSV"):
                results = []

                for _, row in df.iterrows():
                    prediction = classify_email(
                        subject=str(row["subject"]),
                        body=str(row["body"])
                    )

                    results.append({
                        "subject": row["subject"],
                        "body": row["body"],
                        "intent": prediction["intent"],
                        "priority": prediction["priority"],
                        "sentiment": prediction["sentiment"]
                    })

                result_df = pd.DataFrame(results)

                st.subheader("✅ Classification Results")
                st.dataframe(result_df)

                csv = result_df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="⬇️ Download Classified CSV",
                    data=csv,
                    file_name="classified_emails.csv",
                    mime="text/csv"
                )

    except Exception as e:
        st.error(f"Error processing CSV file: {e}")
