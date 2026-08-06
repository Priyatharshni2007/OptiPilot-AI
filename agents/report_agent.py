from utils.gemini import ask_gemini


def generate_report(workflow, roi, risk):

    prompt = f"""
You are an Executive Report AI Agent.

Create a professional consulting report using:

Workflow Analysis:
{workflow}

ROI Analysis:
{roi}

Risk Assessment:
{risk}

Include:

1. Executive Summary
2. Current Problems
3. Automation Recommendations
4. Business Impact
5. Risks
6. Implementation Roadmap

Format like a consulting company report.
"""

    return ask_gemini(prompt)