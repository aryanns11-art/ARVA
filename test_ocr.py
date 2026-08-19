import pyautogui
import time
from windows.ocr import read_text_from_image

time.sleep(3)

screenshot = pyautogui.screenshot()

text = read_text_from_image(screenshot)

print("========== SCREEN TEXT ==========")
print(text)
print("=================================")