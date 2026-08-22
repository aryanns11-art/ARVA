import pyautogui

from windows.ocr import find_text


screenshot = pyautogui.screenshot()

result = find_text(
    screenshot,
    "ARVA"
)


if result:

    confidence = float(result["confidence"])

    if confidence < 70:
        print(f"Low OCR confidence: {confidence}")
        print("Not clicking.")

    x = result["x"]
    y = result["y"]

    print(f"Found text at: ({x}, {y})")
    print(f"Confidence: {confidence}")

    pyautogui.click(x, y)

else:
    print("Text not found.")