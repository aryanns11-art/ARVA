import pyautogui


def type_text(text):

    if not text:
        return False

    print(f"Typing: {text}")

    pyautogui.write(text, interval=0.03)

    return True


def press_key(key):

    if not key:
        return False

    print(f"Pressing: {key}")

    pyautogui.press(key)

    return True