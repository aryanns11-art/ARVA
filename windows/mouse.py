import pyautogui


def click():
    print("Clicking")
    pyautogui.click()
    return True


def double_click():

    print("Double clicking")
    pyautogui.doubleClick()
    return True


def right_click():

    print("Right clicking")
    pyautogui.rightClick()
    return True


def move_mouse(x, y):

    print(f"Moving mouse to: ({x}, {y})")
    pyautogui.moveTo(x, y, duration=0.2)
    return True


def scroll(amount):

    print(f"Scrolling: {amount}")
    pyautogui.scroll(amount)
    return True