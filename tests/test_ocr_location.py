import pyautogui
import time
from windows.ocr import find_text

time.sleep(3)
screenshot = pyautogui.screenshot()

result = find_text(
    screenshot,
    "Hello"
)

if result:

    print("Found:", result)

else:

    print("Text not found.")