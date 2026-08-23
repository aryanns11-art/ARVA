import pyautogui

from windows.ocr import find_best_text
import time

time.sleep(3)
screenshot = pyautogui.screenshot()

result = find_best_text(
    screenshot,
    "hello"
)

if result:

    print("Best match:")
    pyautogui.click(result["x"], result["y"])
    print(result)

else:

    print("No reliable match found.")