import streamlit as st



def show_workflow():

    st.subheader("🧠 Multi-Agent Workflow")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.success("📄\n\nDocument\nIntelligence")

    with c2:
        st.info("⚙️\n\nWorkflow\nAnalysis")

    with c3:
        st.warning("💰\n\nROI\nPrediction")

    with c4:
        st.error("🛡\n\nRisk\nAssessment")

    with c5:
        st.success("📊\n\nExecutive\nReport")

    st.markdown(
        """
        ### ➜ ➜ ➜ ➜ ➜
        """,
        unsafe_allow_html=True
    )