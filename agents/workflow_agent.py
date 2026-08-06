from utils.gemini import ask_gemini


def analyze_workflow(document_text):

    prompt = f"""
You are a Workflow Analysis AI Agent.

Analyze the business process below.

Identify:
- Current workflow
- Bottlenecks
- Manual tasks
- Automation opportunities

Business Process:

{document_text}

Provide a structured business analysis.
"""

    return ask_gemini(prompt)