
import fitz
from docx import Document


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF resume.
    """
    text = ""

    document = fitz.open(file_path)

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_text_from_docx(file_path):
    """
    Extract text from a DOCX resume.
    """
    document = Document(file_path)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    )

    return text


def extract_resume_text(file_path):
    """
    Extract text from a PDF or DOCX resume
    based on its file extension.
    """

    file_path = str(file_path).lower()

    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Please use PDF or DOCX."
        )