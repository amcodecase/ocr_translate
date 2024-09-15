from PIL import Image
import pytesseract

def ocr_image(image):
    # Convert the image to grayscale (if needed) for better OCR results
    image = image.convert('L')
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text
