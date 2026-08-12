from windows.controller import open_app


def execute_command(command):

    if command is None:
        return

    command = command.lower().strip()

    if command.startswith("open "):

        app_name = command[5:].strip()

        if app_name:
            open_app(app_name)
        else:
            print("Which application should I open?")

    else:
        print("I don't know how to do that yet.")