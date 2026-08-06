from utils.gemini import ask_gemini


def analyze_workflow(text):

    prompt = f"""
You are OptiPilot AI, an enterprise automation consultant.

Analyze the following business workflow:

{text}


Return ONLY using this structure:


AUTOMATION SCORE:
Give a score between 0-100 based on automation potential.


WORKFLOW SUMMARY:
Explain the current workflow briefly.


BOTTLENECKS:
List the major inefficiencies.


AUTOMATION OPPORTUNITIES:
Suggest AI and automation solutions.


ROI ESTIMATION:
Mention:
- Time savings
- Cost reduction
- Efficiency improvement


RISKS:
Mention implementation risks.


IMPLEMENTATION ROADMAP:
Give step-by-step implementation phases.


Keep the answer professional for company executives.
Do not add unrelated content.
"""

    response = ask_gemini(prompt)

    return response