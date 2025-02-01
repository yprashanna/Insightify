from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

# Set Tesseract CMD path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def ocr_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

if __name__ == '__main__':
    image_text = ocr_image('test_image.png')
    print("Extracted Text from Image:")
    print(image_text)

    # Uncomment below lines if you have a test PDF
    # pdf_text = ocr_pdf('test_document.pdf')
    # print("Extracted Text from PDF:")
    # print(pdf_text)