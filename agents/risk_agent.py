from utils.gemini import ask_gemini


def analyze_risk(workflow):

    prompt = f"""
You are a Risk Assessment AI Agent.

Analyze this automation workflow:

{workflow}

Identify:

- Technical risks
- Security risks
- Implementation challenges
- Mitigation strategies

Provide a professional risk report.
"""

    return ask_gemini(prompt)