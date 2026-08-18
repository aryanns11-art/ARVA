from parser import parse_command
from windows.controller import ( open_app, open_folder_name, open_file, close_app)
from windows.keyboard import type_text, press_key , press_hotkey
from windows.mouse import ( click, double_click, right_click, scroll  , move_mouse)

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

    else:

        print("I don't know how to do that yet.")