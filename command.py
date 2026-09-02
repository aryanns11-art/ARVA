from parser import parse_command
from windows.controller import ( open_app, open_folder_name, open_file, close_app)
from windows.keyboard import type_text, press_key , press_hotkey
from windows.mouse import ( click, double_click, right_click, scroll  , move_mouse , click_at )
from windows.screen import take_screenshot
from windows.ocr import read_text_from_image, find_best_text
from windows.voice import speak

def execute_command(command):

    result = parse_command(command)

    if result is None:
        return

    intent = result["intent"]
    target = result["target"]

    print("Intent:", intent)
    print("Target:", target)

    if intent == "OPEN_APP":
        open_app(target)

    elif intent == "OPEN_FOLDER":
        open_folder_name(target)

    elif intent == "OPEN_FILE":
        open_file(target)

    elif intent == "CLOSE_APP":
        close_app(target)

    elif intent == "TYPE_TEXT":
        type_text(target)
    
    elif intent == "PRESS_KEY":
        press_key(target)

    elif intent == "PRESS_HOTKEY":
        keys = target.split()
        press_hotkey(keys)

    elif intent == "MOUSE_CLICK":
        click()

    elif intent == "MOUSE_DOUBLE_CLICK":
        double_click()

    elif intent == "MOUSE_RIGHT_CLICK":
        right_click()

    elif intent == "MOUSE_SCROLL":

        if target == "up":
            scroll(5)

        elif target == "down":
            scroll(-5)

        else:
            print("Should I scroll up or down?")

    elif intent == "MOUSE_MOVE":

        x, y = target   
        move_mouse(x, y)

    elif intent == "TAKE_SCREENSHOT":

        screenshot = take_screenshot()
        screenshot.save("screen.png")
        print("Screenshot saved as screen.png")
        speak("Screenshot saved.")

    elif intent == "READ_SCREEN":

        screenshot = take_screenshot()
        text = read_text_from_image(screenshot)

        print("========== SCREEN TEXT ==========")
        print(text)
        print("=================================")

        if text.strip():
            speak(text.strip())
        else:
            speak("I couldn't read any text on the screen.")

    elif intent == "CLICK_TEXT":

        screenshot = take_screenshot()
        result = find_best_text( screenshot, target )

        if result is None:

            print(f"Could not find a reliable match for '{target}'.")
            speak(f"I couldn't find {target}.")
            return

        print(f"Found: {result['text']}")
        print(f"Position: ({result['x']}, {result['y']})")
        print(f"Confidence: {result['confidence']}")

        click_at(result["x"],result["y"])
        speak(f"Clicked {result['text']}.")

    else:
        print("I don't know how to do that yet.")
        speak("I don't know how to do that yet.")