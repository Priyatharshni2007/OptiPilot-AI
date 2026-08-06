from agents.workflow_agent import analyze_workflow
from agents.roi_agent import analyze_roi
from agents.risk_agent import analyze_risk
from agents.report_agent import generate_report


def run_pipeline(document_text):

    print("🚀 Starting Workflow Agent")

    workflow_result = analyze_workflow(
        document_text
    )

    print("✅ Workflow Agent Completed")


    print("🚀 Starting ROI Agent")

    roi_result = analyze_roi(
        workflow_result
    )

    print("✅ ROI Agent Completed")


    print("🚀 Starting Risk Agent")

    risk_result = analyze_risk(
        workflow_result
    )

    print("✅ Risk Agent Completed")


    print("🚀 Starting Report Agent")

    report_result = generate_report(
        workflow_result,
        roi_result,
        risk_result
    )

    print("✅ Report Agent Completed")


    return {
        "workflow": workflow_result,
        "roi": roi_result,
        "risk": risk_result,
        "report": report_result
    }