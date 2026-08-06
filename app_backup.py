import streamlit as st
import os
from utils.document_reader import extract_text
from agents.orchestrator import run_pipeline


# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="OptiPilot AI",
    page_icon="🤖",
    layout="wide"
)


# ----------------------------
# Header
# ----------------------------

st.title("🤖 OptiPilot AI")

st.subheader(
    "AI-powered automation opportunity discovery platform"
)

st.write(
    """
Upload a business document and OptiPilot AI will analyze:

✅ Workflow bottlenecks  
✅ Automation opportunities  
✅ ROI prediction  
✅ Risk assessment  
✅ Executive recommendation report
"""
)


# ----------------------------
# Upload Document
# ----------------------------

uploaded_file = st.file_uploader(
    "Upload Business Document",
    type=["pdf", "docx", "txt"]
)


if uploaded_file:

    # Save uploaded file temporarily

    file_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())


    st.success(
        "Document uploaded successfully"
    )


    # ----------------------------
    # Extract Text
    # ----------------------------

    with st.spinner(
        "Reading document..."
    ):

        document_text = extract_text(
            file_path
        )


    # ----------------------------
    # Run Agents
    # ----------------------------

    if st.button(
        "🚀 Analyze Automation Opportunity"
    ):

        with st.spinner(
            "AI Agents are analyzing..."
        ):

            result = run_pipeline(
                document_text
            )


        st.success(
            "Analysis Completed Successfully"
        )


        # ----------------------------
        # Display Results
        # ----------------------------


        st.divider()

        st.header(
            "🧠 Workflow Analysis"
        )

        st.write(
            result["workflow"]
        )


        st.divider()


        st.header(
            "📊 ROI Prediction"
        )

        st.write(
            result["roi"]
        )


        st.divider()


        st.header(
            "🛡 Risk Assessment"
        )

        st.write(
            result["risk"]
        )


        st.divider()


        st.header(
            "📄 Executive Report"
        )

        st.write(
            result["report"]
        )


        # Download Report

        report_text = result["report"]


        st.download_button(
            label="📥 Download Executive Report",
            data=report_text,
            file_name="OptiPilot_AI_Report.txt",
            mime="text/plain"
        )