import streamlit as st


def executive_dashboard(score):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🤖 Automation Score",
            f"{score}/100"
        )

    with col2:
        st.metric(
            "💰 Estimated ROI",
            "$52.5K"
        )

    with col3:
        if score >= 75:
            risk = "Low"
        elif score >= 50:
            risk = "Medium"
        else:
            risk = "High"

        st.metric(
            "🛡 Risk Level",
            risk
        )

    with col4:
        confidence = min(98, score + 12)

        st.metric(
            "🧠 AI Confidence",
            f"{confidence}%"
        )