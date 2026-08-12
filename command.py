from windows.controller import open_app


def execute_command(command):

    fcommand = command.lower()

    if fcommand is None:
        return

    if "open chrome" in fcommand:
        open_app("chrome")

    elif "open kiro" in fcommand:
        open_app("kiro")

    elif "open postman" in fcommand:
        open_app("postman")

    elif "open notepad" in fcommand:
        open_app("notepad")

    else:
        print("I don't know how to do that yet.")