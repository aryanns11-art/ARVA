import os
import subprocess
from pathlib import Path
import shutil

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
    print("Searching for:", name)

    if shortcut is not None:

        print("Found:", shortcut)
        print("Opening:", shortcut)

        os.startfile(shortcut)
        return

    executable = shutil.which(name)

    if executable is not None:

        print("Found executable:", executable)
        print("Opening:", executable)

        subprocess.Popen([executable])
        return

    print("Error: Application not found!")

#---------------------------------------------

SPECIAL_FOLDERS = {
    "downloads": Path.home() / "Downloads",
    "documents": Path.home() / "Documents",
    "desktop": Path.home() / "Desktop",
    "pictures": Path.home() / "Pictures",
    "videos": Path.home() / "Videos",
}

def open_folder_name(name):

    name = name.lower().strip()

    if name not in SPECIAL_FOLDERS:
        print("Error: Folder not found!")
        return

    folder = SPECIAL_FOLDERS[name]

    if not folder.exists():
        print("Error: Folder does not exist!")
        return

    os.startfile(folder)
