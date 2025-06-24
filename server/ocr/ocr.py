"""
Use pytesseract to comprehend .pdf and hopefully extract data as-is.
"""
from PIL import Image
import pytesseract
from typing import Any

"""Super prim pdf reader for tesseract"""
def read_pdf(file_path: str):

    pytesseract.image_to_string(file_path)


    

