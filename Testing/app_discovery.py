from pathlib import Path
import os


USER_PROGRAMS = Path(os.environ["APPDATA"]) / "Microsoft/Windows/Start Menu/Programs"

SYSTEM_PROGRAMS = Path(os.environ["ProgramData"]) / "Microsoft/Windows/Start Menu/Programs"


def find_apps():

    shortcuts = []

    for folder in [USER_PROGRAMS, SYSTEM_PROGRAMS]:

        for shortcut in folder.rglob("*.lnk"):
            shortcuts.append(shortcut)

    return shortcuts


apps = find_apps()

for app in apps:
    print(app.name)

