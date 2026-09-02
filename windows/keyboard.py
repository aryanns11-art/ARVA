import pyautogui

from windows.voice import speak


def normalize_key(key):

    key_aliases = {
        "control": "ctrl",
        "escape": "esc",
        "windows": "win",
        "return": "enter",
    }

    return key_aliases.get(key.lower(), key.lower())

def type_text(text):

    if not text:
        return False

    print(f"Typing: {text}")

    pyautogui.write(text, interval=0.03)
    speak("Typing the text.")

    return True


def press_key(key):

    if not key:
        return False

    key = normalize_key(key)

    print(f"Pressing: {key}")

    pyautogui.press(key)
    speak(f"Pressing {key}.")

    return True

def press_hotkey(keys):

    if not keys:
        return False

    keys = [normalize_key(key) for key in keys]
        
    print(f"Pressing combination: {' + '.join(keys)}")

    pyautogui.hotkey(*keys)
    speak(f"Pressing {' plus '.join(keys)}.")

    return True