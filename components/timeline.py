import streamlit as st
import datetime
import time


def show_timeline():

    st.subheader("🤖 AI Agent Timeline")

    agents = [

        "📄 Document Intelligence",

        "⚙ Workflow Analysis",

        "💰 ROI Prediction",

        "🛡 Risk Assessment",

        "📊 Executive Report"

    ]

    timeline = st.empty()

    history = ""

    for agent in agents:

        now = datetime.datetime.now().strftime("%H:%M:%S")

        history += f"""
🟢 {now}

{agent}

✅ Completed

---

"""

        timeline.markdown(history)

        time.sleep(0.6)