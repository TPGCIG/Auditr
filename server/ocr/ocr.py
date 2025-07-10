"""
Use pypdf to comprehend .pdf and hopefully extract data as-is.
"""
from typing import List
import pypdf
from PIL import Image
import os

print("Current Working Directory:", os.getcwd())

def read_pdf(file_path: str) -> str:
    """Extracts text from a PDF file using OCR (Tesseract)"""

    # Convert PDF pages to images
    pages: List[Image.Image] = convert_from_path(file_path)

    # Run OCR on each image
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)

    return text