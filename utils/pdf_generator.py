from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import markdown
import re

def clean_markdown(text):

    if text is None:
        return ""

    text = str(text)

    # Remove ALL HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove markdown symbols
    text = text.replace("**", "")
    text = text.replace("##", "")
    text = text.replace("#", "")

    # Replace bullets
    text = text.replace("•", "-")

    # Remove extra spaces
    text = re.sub(r"\n\s*\n", "\n\n", text)

    return text


def generate_pdf(result):
    print(result.keys())
    print("========== REPORT START ==========")
    print(repr(result.get("report")))
    print("========== REPORT END ==========")

    file_path = "OptiPilot_Enterprise_Report.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    story = []


    story.append(
        Paragraph(
            "OptiPilot AI - Enterprise Executive Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))


    sections = [
    ("Workflow Analysis", result.get("workflow", "")),
    ("ROI Prediction", result.get("roi", "")),
    ("Risk Assessment", result.get("risk", "")),
    ("Executive Report", result.get("report", ""))
    ]


    for heading, content in sections:

        story.append(
            Paragraph(
                heading,
                styles["Heading2"]
            )
        )

        formatted_text = clean_markdown(content)

        story.append(
            Paragraph(
                formatted_text.replace("\n", "<br/>"),
                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1,15)
        )

    print(result.keys())
    print(result.keys())
    doc.build(story)

    return file_path