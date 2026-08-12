from windows.controller import open_app
from windows.controller import open_app, open_folder_name, open_path


def execute_command(command):

    if command is None:
        return

    command = command.lower().strip()

    if not command.startswith("open "):
        print("I don't know how to do that yet.")
        return

    target = command[5:].strip()

    if not target:
        print("What should I open?")
        return

    if target in ["downloads", "documents", "desktop", "pictures", "videos"]:
        open_folder_name(target)
        return

    open_app(target)