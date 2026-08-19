import pyautogui


def get_screen_size():

    width, height = pyautogui.size()

    print(f"Screen size: {width} x {height}")

    return width, height


def take_screenshot():

    screenshot = pyautogui.screenshot()

    print("Screenshot captured.")

    return screenshot