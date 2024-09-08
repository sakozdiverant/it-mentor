import pytesseract

document = "documents/221.jpg"

try:
    extracted_text = pytesseract.image_to_string(document)
    print(extracted_text)
except Exception as e:
    print(f"Error in Tesseract OCR: {str(e)}")

