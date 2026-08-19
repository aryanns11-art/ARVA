import pytesseract


def read_text_from_image(image):

    text = pytesseract.image_to_string(image)

    return text