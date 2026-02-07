import os
import pdfplumber
from docx import Document


def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text


def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_text_from_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_text(path):
    ext = os.path.splitext(path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(path)

    elif ext == ".docx":
        return extract_text_from_docx(path)

    elif ext == ".txt":
        return extract_text_from_txt(path)

    else:
        raise ValueError("Unsupported file type")
