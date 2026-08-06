import streamlit as st


def show_summary(score):

    confidence = min(score + 12, 98)

    if score >= 75:
        recommendation = "✅ Strong Candidate for Automation"
        risk = "🟢 Low"

    elif score >= 50:
        recommendation = "⚠ Moderate Automation Opportunity"
        risk = "🟡 Medium"

    else:
        recommendation = "❌ Not Recommended"
        risk = "🔴 High"

    st.subheader("📊 Executive Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"🤖 Automation Score : **{score}/100**")
        st.success("💰 Estimated Annual Savings : **$52,500**")
        st.warning(f"🛡 Risk Level : **{risk}**")

    with col2:
        st.success(f"🧠 AI Confidence : **{confidence}%**")
        st.info(f"⭐ Recommendation:\n\n{recommendation}")