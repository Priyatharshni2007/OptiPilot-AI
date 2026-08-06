from utils.gemini import ask_gemini


def analyze_roi(workflow):

    prompt = f"""
You are an ROI Prediction AI Agent.

Based on this workflow analysis:

{workflow}

Estimate:

- Time savings
- Cost reduction
- Efficiency improvement
- Automation score

Give a business-friendly ROI report.
"""

    return ask_gemini(prompt)