import pyautogui

from windows.voice import speak


def click():
    print("Clicking")
    pyautogui.click()
    speak("Clicking.")
    return True

def click_at(x, y):

    print(f"Clicking at: ({x}, {y})")

    pyautogui.click(x, y)

def double_click():

    print("Double clicking")
    pyautogui.doubleClick()
    speak("Double clicking.")
    return True


def right_click():

    print("Right clicking")
    pyautogui.rightClick()
    speak("Right clicking.")
    return True


def move_mouse(x, y):

    print(f"Moving mouse to: ({x}, {y})")
    pyautogui.moveTo(x, y, duration=0.2)
    speak("Moving the mouse.")
    return True


def scroll(amount):

    print(f"Scrolling: {amount}")
    pyautogui.scroll(amount)
    speak("Scrolling up." if amount > 0 else "Scrolling down.")
    return True

def move_mouse(x, y):

    print(f"Moving mouse to: ({x}, {y})")
    pyautogui.moveTo(x, y, duration=0.2)
    speak("Moving the mouse.")
    return True