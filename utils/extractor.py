from pypdf import PdfReader
from docx import Document


def extract_text(file):
    """
    Extract text from PDF or DOCX files uploaded through Streamlit.
    """
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    elif filename.endswith(".docx"):
        doc = Document(file)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)

    return ""