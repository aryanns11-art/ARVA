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


def open_file(path):

    path = Path(path)

    if not path.exists():
        print("Error: File does not exist!")
        return

    if not path.is_file():
        print("Error: Path is not a file!")
        return

    os.startfile(path)

APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
}

def open_app(name):

    name = name.lower()

    if name not in APPS:
        print("Error: Application not found.")
        return

    subprocess.Popen([APPS[name]])