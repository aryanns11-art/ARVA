import pyautogui

from windows.ocr import find_all_text

import time

time.sleep(3)

screenshot = pyautogui.screenshot()

results = find_all_text(
    screenshot,
    "open"
)                                                                             

if not results:

    print("Text not found.")

else:

    print(f"Found {len(results)} matches.")

    for result in results:

        print(result)
        pyautogui.click(result["x"], result["y"])