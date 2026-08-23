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
                "confidence": float(data["conf"][i])
            }

    return None


def find_all_text(image, target):

    data = pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT
    )

    target = target.lower().strip()

    results = []

    for i, word in enumerate(data["text"]):

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

            confidence = float(data["conf"][i])

            results.append({
                "text": word,
                "x": center_x,
                "y": center_y,
                "width": width,
                "height": height,
                "confidence": confidence
            })

    return results



def find_best_text(image, target, min_confidence=70):

    results = find_all_text(image, target)

    valid_results = [
        result
        for result in results
        if result["confidence"] >= min_confidence
    ]

    if not valid_results:
        return None

    return max(
        valid_results,
        key=lambda result: result["confidence"]
    )