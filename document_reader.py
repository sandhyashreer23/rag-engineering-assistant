from PyPDF2 import PdfReader
from docx import Document


def read_pdf(uploaded_file):
    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text


def read_docx(uploaded_file):
    doc = Document(uploaded_file)

    text = "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )

    return text