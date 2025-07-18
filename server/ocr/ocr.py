"""
Use pypdf to comprehend .pdf and hopefully extract data as-is.
"""
from typing import List
import pypdf
from PIL import Image
import os

print("Current Working Directory:", os.getcwd())

def read_pdf(file_path: str) -> str:
    """Extracts text from a PDF file using pdypdf"""

    # Convert PDF pages to images
    pdf_reader = pypdf.PdfReader(file_path)