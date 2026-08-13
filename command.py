from parser import parse_command
from windows.controller import (
    open_app,
    open_folder_name,
    open_file,
    close_app,
)


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

    else:

        print("I don't know how to do that yet.")