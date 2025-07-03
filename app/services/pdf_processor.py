from PyPDF2 import PdfReader
from fastapi import UploadFile

async def extract_text_from_pdf(file: UploadFile) -> str:
    content = await file.read()
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
