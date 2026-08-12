import os
import subprocess
from pathlib import Path


def open_folder(path):

    path = Path(path)

    if not path.exists():
        print("Error: Folder does not exist!")
        return

    if not path.is_dir():
        print("Error: Path is not a folder!")
        return

    os.startfile(path)

#--------------------------------------------------------------------

def open_file(path):

    path = Path(path)

    if not path.exists():
        print("Error: File does not exist!")
        return

    if not path.is_file():
        print("Error: Path is not a file!")
        return

    os.startfile(path)

#--------------------------------------------------------------------

USER_PROGRAMS = (Path(os.environ["APPDATA"])/ "Microsoft/Windows/Start Menu/Programs")  
SYSTEM_PROGRAMS = (Path(os.environ["ProgramData"])/ "Microsoft/Windows/Start Menu/Programs")


def find_app(name):

    name = name.lower()

    for folder in [USER_PROGRAMS, SYSTEM_PROGRAMS]:

        for shortcut in folder.rglob("*.lnk"):

            if name in shortcut.stem.lower():
                return shortcut

    return None

def open_app(name):

    shortcut = find_app(name)

    if shortcut is None:
        print("Error: Application not found!")
        return

    os.startfile(shortcut)