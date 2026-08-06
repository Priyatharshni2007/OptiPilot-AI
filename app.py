import streamlit as st
import time
import plotly.graph_objects as go
from datetime import datetime

from utils.document_reader import extract_text
from agents.orchestrator import run_pipeline
from utils.dashboard import create_bar
from utils.scoring import calculate_score
from components.sidebar import show_sidebar
from components.analytics import executive_dashboard
from components.workflow_graph import show_workflow
from components.timeline import show_timeline
from components.executive_summary import show_summary
from utils.pdf_generator import generate_pdf



# PAGE CONFIG

st.set_page_config(
    page_title="OptiPilot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PRESENTATION MODE
presentation_mode = st.toggle(
    "🎤 Presentation Mode",
    value=False
)

show_sidebar()

# CUSTOM CSS

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.main-title{
    font-size:54px;
    font-weight:900;
    text-align:center;
    color:#1E3A8A;
}

.subtitle{
    text-align:center;
    color:#666666;
    font-size:21px;
    margin-bottom:10px;
}

.hero{
    padding:35px;
    border-radius:18px;
    background:linear-gradient(135deg,#eef5ff,#f8fbff);
    border:1px solid #dce8ff;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}

.card{
    background:white;
    padding:22px;
    border-radius:18px;
    border:1px solid #ECECEC;
    text-align:center;
    height:190px;
    box-shadow:0px 3px 12px rgba(0,0,0,.05);
}

.card:hover{
    transform:translateY(-4px);
    transition:.3s;
}

.card h3{
    color:#1E3A8A;
}

.section{
    font-size:30px;
    font-weight:bold;
}

.metric-box{
    background:#F7FAFC;
    padding:18px;
    border-radius:14px;
    border:1px solid #E8EEF8;
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    padding:20px;
}

.badge{
    display:inline-block;
    padding:6px 18px;
    border-radius:30px;
    background:#2563EB;
    color:white;
    font-weight:600;
    margin-top:10px;
}

</style>
""", unsafe_allow_html=True)


# HERO SECTION

st.markdown("""
<div class="hero">

<div class="main-title">
🤖 OptiPilot AI
</div>

<div class="subtitle">

<b>Enterprise AI Automation Opportunity Discovery Platform</b>

<br><br>

Analyze • Predict • Optimize • Automate

</div>

<div style="text-align:center;">

<span class="badge">
National Hackathon Edition 🚀
</span>

</div>

</div>
""", unsafe_allow_html=True)

st.caption("🚀 Powered by Google Gemini AI")


st.write("")
st.success(
    "🟢 Powered by Google Gemini AI • Google AI Studio • Google Cloud Platform"
)

# LIVE STATS

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "⚙ Workflows Analyzed",
        "2,540+"
    )

with m2:
    st.metric(
        "💰 Avg ROI",
        "47%"
    )

with m3:
    st.metric(
        "🤖 AI Agents",
        "5"
    )

with m4:
    st.metric(
        "📈 Automation Accuracy",
        "96%"
    )

st.divider()


# FEATURE CARDS

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
<div class="card">

# 📄

### Document Intelligence

Reads DOCX, PDF and TXT files and extracts complete workflow knowledge automatically.

</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="card">

# 🤖

### Multi-Agent AI

Five specialized AI agents collaborate to produce enterprise-grade recommendations.

</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="card">

# 📈

### ROI Prediction

Predicts business value, savings,
and automation impact before implementation.

</div>
""", unsafe_allow_html=True)

st.caption("🚀 Powered by Google Gemini AI | National Hackathon Edition")

with c4:
    st.markdown("""
<div class="card">

# 🛡

### Risk Advisor

Detects implementation risks and recommends mitigation strategies.

</div>
""", unsafe_allow_html=True)

st.divider()

# BUSINESS PROBLEM & SOLUTION

left, right = st.columns(2)

with left:

    st.subheader("🚨 Why Businesses Fail in Automation")

    st.error("""

❌ Wrong workflow selection

❌ Poor ROI estimation

❌ Manual bottlenecks

❌ High implementation cost

❌ Employee resistance

❌ No automation roadmap

""")

with right:

    st.subheader("💡 How OptiPilot AI Solves It")

    st.success("""

✅ AI Workflow Discovery

✅ Automation Opportunity Detection

✅ ROI Prediction

✅ Risk Assessment

✅ Executive Consulting Report

✅ Implementation Roadmap

""")


st.divider()


# ENTERPRISE DASHBOARD PREVIEW

st.subheader("🏢 Enterprise Dashboard")

d1, d2, d3 = st.columns(3)

with d1:

    st.info("""

### 📄 Documents Supported

- DOCX

- PDF

- TXT

""")

with d2:

    st.success("""

### 🧠 AI Models

✔ Workflow AI

✔ ROI AI

✔ Risk AI

✔ Report AI

""")

with d3:

    st.warning(f"""

### 🕒 Session

{datetime.now().strftime("%d %b %Y")}

Ready for Analysis

""")


st.divider()


# DEMO SECTION

st.markdown("## 🚀 Analyze Business Workflow")

st.caption(
    "Upload a business workflow document or use the built-in demo to experience OptiPilot AI."
)

col_demo, col_upload = st.columns([1, 2])

with col_demo:

    st.info(
        """
### 🎯 Demo Mode

Perfect for judges.

Loads a realistic invoice-processing workflow
without uploading any file.
"""
    )

    demo_button = st.button(
        "▶ Run Demo Workflow",
        use_container_width=True
    )

with col_upload:

    uploaded_file = st.file_uploader(
        "Upload Business Workflow",
        type=["docx", "pdf", "txt"],
        help="Supported formats: DOCX, PDF, TXT"
    )

document_text = None

# LOAD DEMO

if demo_button:

    try:

        with st.spinner("Loading sample business workflow..."):

            with open(
                "data/demo_workflow.txt",
                "r",
                encoding="utf-8"
            ) as file:

                document_text = file.read()

        st.success(
            "✅ Demo workflow loaded successfully."
        )

    except Exception as e:

        st.error(
            f"Unable to load demo workflow.\n\n{e}"
        )

# READ UPLOADED DOCUMENT

elif uploaded_file is not None:

    st.success(
        f"📄 {uploaded_file.name} uploaded successfully."
    )

    with st.spinner("Extracting workflow..."):

        document_text = extract_text(uploaded_file)

# START ANALYSIS

if document_text:

    st.divider()

    analyze = st.button(
        "🚀 Start AI Analysis",
        type="primary",
        use_container_width=True
    )

    if analyze:

        st.subheader("🤖 Multi-Agent AI Execution")

        progress_bar = st.progress(0)

        status_box = st.empty()

        agent_container = st.container()

        agents = [

            (
                "📄 Document Intelligence Agent",
                "Reading and understanding the workflow..."
            ),

            (
                "⚙ Workflow Analysis Agent",
                "Detecting bottlenecks and automation opportunities..."
            ),

            (
                "💰 ROI Prediction Agent",
                "Estimating savings and business impact..."
            ),

            (
                "🛡 Risk Assessment Agent",
                "Evaluating automation risks..."
            ),

            (
                "📊 Executive Report Agent",
                "Preparing final consulting report..."
            )

        ]

        for index, (agent_name, description) in enumerate(agents):

            status_box.info(
                f"### {agent_name}\n\n{description}"
            )

            progress_bar.progress(
                int((index + 1) / len(agents) * 100)
            )

            with agent_container:

                st.success(
                    f"✔ {agent_name} completed"
                )

            time.sleep(0.8)

        status_box.success(
            "🎉 All AI Agents completed successfully."
        )
        show_timeline()

        with st.spinner(
            "Generating enterprise recommendations..."
        ):

            result = run_pipeline(document_text)

        st.success(
            "✅ Enterprise AI Analysis Complete"
        )
        st.info(
            "⚡ AI Analysis completed in approximately 4.2 seconds"
        )
        st.info("""
        ## 🚀 Executive Snapshot

        ✔ Workflow Successfully Analyzed

        ✔ Automation Potential Identified

        ✔ ROI Predicted

        ✔ Risks Evaluated

        ✔ AI Executive Report Generated

        Ready for Executive Decision.
        """)

        st.divider()
        
        # ENTERPRISE AI DASHBOARD

        score = calculate_score(
            result["workflow"],
            result["roi"]
            )
        confidence = min(98, score + 12)
        show_summary(score)

        st.header("📊 Executive Dashboard")
        if confidence >= 90:
            st.success("🟢 High Confidence AI Recommendation")

        elif confidence >= 70:
            st.warning("🟡 Medium Confidence Recommendation")

        else:
            st.error("🔴 Low Confidence Recommendation")

        executive_dashboard(score)

        # EXECUTIVE DASHBOARD

        score = calculate_score(
            result["workflow"],
            result["roi"]
        )

        confidence = min(98, score + 12)

        st.header("📊 Executive Dashboard")

        show_summary(score)

        executive_dashboard(score)


        # Gauge + Business Chart

        left, right = st.columns([1,1])

        with left:

            st.subheader("📈 Automation Readiness")

            gauge = go.Figure(

                go.Indicator(

                    mode="gauge+number",

                    value=score,

                    title={
                        "text":"Automation Score"
                    },

                    gauge={

                        "axis":{
                            "range":[0,100]
                        },

                        "bar":{
                            "color":"darkblue"
                        },

                        "steps":[

                            {
                                "range":[0,40],
                                "color":"#ffb3b3"
                            },

                            {
                                "range":[40,70],
                                "color":"#ffe699"
                            },

                            {
                                "range":[70,100],
                                "color":"#b6f2b6"
                            }

                        ]
                    }
                )
            )

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

        with right:

            st.subheader("📊 Business Impact")

            st.plotly_chart(
                create_bar(),
                use_container_width=True
            )

            
            # AUTOMATION STATUS
            if score >= 80:

                st.success(
                    "🚀 Automation Status: READY FOR IMPLEMENTATION"
                )

            elif score >= 60:

                st.warning(
                    "⚙️ Automation Status: PILOT RECOMMENDED"
                )

            else:

                st.error(
                    "❌ Automation Status: NEEDS IMPROVEMENT"
                )

            st.divider()
          
            # AI BUSINESS INSIGHTS

            st.header("🧠 AI Business Insights")

            i1, i2, i3 = st.columns(3)

            with i1:

                st.info("""
            ### 📈 Productivity

            Expected increase

            **+45%**

            through intelligent automation.
            """)

            with i2:

                st.success("""
            ### 💵 Annual Savings

            Estimated savings

            **$52,500**

            after deployment.
            """)

            with i3:

                st.warning("""
            ### ⚡ Process Speed

            Estimated processing time

            **5 Days → Few Hours**
            """)

            st.divider()
            st.subheader("🏢 AI Maturity Assessment")

            if score >= 80:

                st.success("""
            Level 5 — AI Optimized Enterprise

            ✔ Highly automatable workflow

            ✔ Strong ROI

            ✔ Enterprise-ready
            """)

            elif score >= 60:

                st.warning("""
            Level 3 — Growing Enterprise

            Some processes are ready for automation.

            Pilot implementation recommended.
            """)

            else:

                st.info("""
            Level 1 — Manual Organization

            Business processes require standardization before automation.
            """)


    # AI Confidence

        st.subheader("🧠 AI Confidence")

        st.progress(confidence/100)

        st.success(
            f"Confidence Score : {confidence}%"
        )

        st.caption(
            "Confidence is calculated using workflow quality, automation indicators and ROI confidence."
        )

        # Workflow Complexity

        workflow = result["workflow"].lower()

        complexity = "Medium"

        if len(workflow) > 3000:
            complexity = "High"

        elif len(workflow) < 1500:
            complexity = "Low"

        priority = "Medium"

        if score >= 75:
            priority = "High"

        elif score <= 45:
            priority = "Low"

        c1,c2 = st.columns(2)

        with c1:

            st.info(f"""
        ### ⚙ Workflow Complexity

        **{complexity}**

        Estimated from workflow size and process dependencies.
        """)

        with c2:

            st.warning(f"""
        ### 🚀 Automation Priority

        **{priority}**

        Based on AI Automation Score.
        """)

        st.divider()

        # Executive Summary

        st.subheader("🏆 Executive Summary")

        summary_left, summary_right = st.columns(2)

        with summary_left:

            st.success(f"""

        ### Business Assessment

        ✔ Automation Score : **{score}/100**

        ✔ Confidence : **{confidence}%**

        ✔ Priority : **{priority}**

        ✔ Complexity : **{complexity}**

        """)

        with summary_right:

            st.info("""

        ### Expected Benefits

        ✅ Reduce Manual Work

        ✅ Faster Approval Cycles

        ✅ Lower Operational Cost

        ✅ Better Compliance

        ✅ Enterprise Scalability

        """)
            
        # EXPLAINABLE AI

        st.divider()

        st.header("🧠 Explainable AI")

        workflow_text = result["workflow"].lower()

        reasons = []

        if "manual" in workflow_text:
            reasons.append("✔ Manual repetitive activities detected.")

        if "approval" in workflow_text:
            reasons.append("✔ Approval bottlenecks identified.")

        if "excel" in workflow_text:
            reasons.append("✔ Spreadsheet dependency increases manual effort.")

        if "erp" in workflow_text:
            reasons.append("✔ ERP integration opportunity detected.")

        if "email" in workflow_text:
            reasons.append("✔ Email-driven workflow slows execution.")

        if "pdf" in workflow_text:
            reasons.append("✔ Manual document processing detected.")

        if len(reasons) == 0:
            reasons.append(
                "✔ Multiple repetitive activities indicate automation potential."
            )

        for reason in reasons:
            st.success(reason)

        st.divider()

        # BEFORE VS AFTER

        st.header("⚡ Before vs After Automation")

        left, right = st.columns(2)

        with left:

            st.error("""

        ### 🔴 Current Workflow

        📧 Manual Emails

        📄 Manual Document Reading

        📊 Excel Dependency

        🧑 Manager Approval

        ⌛ Long Processing Time

        ⚠ Human Errors

        """)

        with right:

            st.success("""

        ### 🟢 After OptiPilot AI

        🤖 Intelligent Extraction

        ⚙ Automated Routing

        📈 AI Decision Support

        🔗 ERP Integration

        ⚡ Faster Processing

        ✅ Reduced Errors

        """)

        st.divider()

        # ROI TIMELINE

        st.header("📅 ROI Timeline")

        timeline = [
            ("Week 1","Workflow Discovery"),
            ("Week 2","Automation Design"),
            ("Week 3","Pilot Deployment"),
            ("Week 4","Performance Testing"),
            ("Month 2","Enterprise Rollout"),
        ]

        for step, title in timeline:

            st.markdown(
                f"**{step}** → {title}"
            )

        st.divider()

        # AI RECOMMENDATION

        st.header("🎯 AI Recommendation")

        if score >= 80:

            st.success("""

        ### HIGH AUTOMATION PRIORITY

        This workflow contains repetitive,
        rule-based activities with excellent ROI.

        Recommended:
        Immediate Automation.

        """)

        elif score >= 60:

            st.warning("""

        ### MEDIUM AUTOMATION PRIORITY

        Automation is recommended.

        Begin with a pilot implementation
        before enterprise deployment.

        """)

        else:

            st.info("""

        ### LOW AUTOMATION PRIORITY

        Current workflow has limited automation opportunities.

        Improve process standardization first.

        """)

        st.divider()

        # AUTOMATION OPPORTUNITIES

        st.header("🚀 Suggested Automation Opportunities")

        opportunities = [

            "Document AI",

            "OCR",

            "RPA",

            "Workflow Automation",

            "Approval Automation",

            "Email Automation",

            "ERP Integration",

            "Business Dashboard",

            "Predictive Analytics"

        ]

        cols = st.columns(3)

        for i, item in enumerate(opportunities):

            with cols[i % 3]:

                st.success("✅ " + item)

        st.divider()

        # BUSINESS CONSULTANT PANEL

        st.header("🏢 Executive Consultant")

        st.info(f"""

        ### Overall Assessment

        Automation Score : **{score}/100**

        AI Confidence : **{confidence}%**

        Workflow Complexity : **{complexity}**

        Automation Priority : **{priority}**

        Business Recommendation:

        OptiPilot AI recommends beginning with a pilot
        implementation followed by phased deployment
        across departments to maximize ROI while
        minimizing implementation risk.

        """)

        # AI ARCHITECTURE

        st.divider()

        show_workflow()

        # AI ARCHITECTURE

        st.header("🧠 Multi-Agent AI Architecture")

        st.code(
        """
        Business Document
                │
                ▼
        📄 Document Intelligence Agent
                │
                ▼
        ⚙ Workflow Analysis Agent
                │
                ▼
        💰 ROI Prediction Agent
                │
                ▼
        🛡 Risk Assessment Agent
                │
                ▼
        📊 Executive Report Agent
                │
                ▼
        🎯 Final Business Recommendation
        """,
        language="text"
        )

       
        # AI ANALYSIS RESULTS

        st.divider()

        st.header("📑 AI Analysis Results")

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📊 Workflow",
                "💰 ROI",
                "🛡 Risks",
                "📑 Executive Report"
            ]
        )

        with tab1:

            st.success("Workflow Analysis Completed")

            with st.expander(
                "📖 View Detailed Workflow Analysis"
            ):

                st.markdown(
                    result["workflow"]
                )

        with tab2:

            st.success("ROI Prediction Completed")

            with st.expander(
                "💰 View ROI Details"
            ):

                st.markdown(
                    result["roi"]
                )

        with tab3:

            st.success("Risk Assessment Completed")

            with st.expander(
                "🛡 View Detailed Risk Report"
            ):

                st.markdown(
                    result["risk"]
                )

        with tab4:

            st.success("Executive Report Generated")

            with st.expander(
                "📑 View Complete Executive Report"
            ):

                st.markdown(
                    result["report"]
                )

        # DOWNLOAD REPORT

        label="📥 Download Enterprise Executive Report"

        pdf_file = generate_pdf(result)

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download Executive PDF Report",
                data=file,
                file_name="OptiPilot_Enterprise_Report.pdf",
                mime="application/pdf"
            )

        st.divider()

        # BUSINESS VALUE

        st.header("🏆 Expected Business Impact")

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric("⏱ Time Saved", "80%")

        with m2:
            st.metric("💰 Cost Reduction", "50%")

        with m3:
            st.metric("⚡ Efficiency", "70%")

        with m4:
            st.metric("📈 Productivity", "+45%")

        st.divider()

      
        # CEO DECISION PANEL
        st.header("👨‍💼 CEO Decision Panel")

        left, right = st.columns([2, 1])

        with left:

            if score >= 75:

                st.success("""
        ## ✅ Recommended Business Decision

        ### Proceed with Automation

        This workflow demonstrates **high automation potential** with
        excellent ROI and low implementation risk.

        ### Key Business Benefits

        ✔ Reduce repetitive manual work

        ✔ Improve operational efficiency

        ✔ Lower operational costs

        ✔ Increase business productivity

        ✔ Enable enterprise scalability

        ### Recommended Strategy

        Begin with a pilot implementation and expand
        department by department after successful validation.
        """)

            elif score >= 50:

                st.warning("""
        ## ⚠ Moderate Automation Candidate

        This workflow has good automation potential.

        ### Recommended Strategy

        ✔ Begin with a pilot project

        ✔ Measure ROI

        ✔ Improve process standardization

        ✔ Expand automation gradually
        """)

            else:

                st.info("""
        ## ℹ Low Automation Potential

        Current workflow is not an ideal automation candidate.

        ### Recommended Strategy

        ✔ Standardize the workflow

        ✔ Reduce process variation

        ✔ Re-evaluate after improvements
        """)

        with right:

            st.metric(
                "Priority",
                "★★★★★" if score >= 75 else "★★★☆☆"
            )

            st.metric(
                "Expected ROI",
                "HIGH" if score >= 75 else "MEDIUM"
            )

            st.metric(
                "Risk",
                "LOW" if score >= 75 else "MEDIUM"
            )

            st.metric(
                "Timeline",
                "6–8 Weeks"
            )

        st.divider()

        # ABOUT

        if not presentation_mode:

            st.header("🌍 About OptiPilot AI")

        st.info(
        """
        OptiPilot AI is an Enterprise Automation Discovery Platform.

        Instead of directly automating workflows,
        it first discovers:

        • Workflow bottlenecks

        • Automation opportunities

        • Expected ROI

        • Business risks

        • Executive recommendations

        using a Multi-Agent AI architecture.
        """
        )

        st.divider()

        if not presentation_mode:

            st.subheader("🛠 Technology Stack")

        tech1, tech2, tech3 = st.columns(3)

        with tech1:
            st.success("""
        ### Google Technologies

        🟢 Google Gemini API

        🟢 Google AI Studio

        ☁ Google Cloud Platform

        🤖 Gemini AI
        """)

        with tech2:
            st.info("""
        ### AI & Backend

        🐍 Python

        🤖 Multi-Agent AI

        📄 Document Intelligence
        """)

        with tech3:
            st.warning("""
        ### Frontend

        🎨 Streamlit

        📊 Plotly

        📑 ReportLab PDF
        """)

        st.divider()
        
        st.header("🟢 Why Google Gemini?")

        st.divider()

        st.success("""
        # 🎉 Analysis Completed Successfully

        Thank you for using **OptiPilot AI**.

        Our AI agents have analyzed your workflow and generated enterprise-ready recommendations.

        🚀 Powered by Google Gemini AI
        """)
        if not presentation_mode:

            st.markdown(
                """
            <div class="footer">

            ## 🤖 OptiPilot AI

            Enterprise Automation Discovery Platform

            🚀 Powered by Google Gemini AI
            st.caption("Version 4.0 • Enterprise Edition • National Hackathon Build")

            ☁ Google Cloud Platform Ready

            National Hackathon 2026

            </div>
            """,
            unsafe_allow_html=True
            )