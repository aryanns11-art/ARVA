import pytesseract


def read_text_from_image(image):

    text = pytesseract.image_to_string(image)

    return text


def find_text(image, target):

    data = pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT
    )

    target = target.lower().strip()

    words = data["text"]

    for i, word in enumerate(words):

        word = word.strip()

        if not word:
            continue

        if target in word.lower():

            x = data["left"][i]
            y = data["top"][i]
            width = data["width"][i]
            height = data["height"][i]

            center_x = x + width // 2
            center_y = y + height // 2

            return {
                "text": word,
                "x": center_x,
                "y": center_y,
                "width": width,
                "height": height,
                "confidence": data["conf"][i]
            }

    return None