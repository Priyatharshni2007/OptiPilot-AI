import docx
import PyPDF2


def extract_text(uploaded_file):

    file_name = uploaded_file.name


    # DOCX FILE
    if file_name.endswith(".docx"):

        document = docx.Document(uploaded_file)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text



    # PDF FILE
    elif file_name.endswith(".pdf"):

        pdf_reader = PyPDF2.PdfReader(
            uploaded_file
        )

        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text()

        return text



    # TXT FILE
    elif file_name.endswith(".txt"):

        return uploaded_file.read().decode(
            "utf-8"
        )



    else:

        return "Unsupported file format"