import os
import shutil
import subprocess
from pathlib import Path


USER_PROGRAMS = (Path(os.environ["APPDATA"])/ "Microsoft/Windows/Start Menu/Programs")
SYSTEM_PROGRAMS = (Path(os.environ["ProgramData"])/ "Microsoft/Windows/Start Menu/Programs")

SPECIAL_FOLDERS = {
    "downloads": Path.home() / "Downloads",
    "documents": Path.home() / "Documents",
    "desktop": Path.home() / "Desktop",
    "pictures": Path.home() / "Pictures",
    "videos": Path.home() / "Videos",
}


def find_app(name):

    name = name.lower().strip()

    for folder in [USER_PROGRAMS, SYSTEM_PROGRAMS]:

        if not folder.exists():
            continue

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
        return True

    executable = shutil.which(name)

    if executable is not None:

        print("Found executable:", executable)
        print("Opening:", executable)

        subprocess.Popen([executable])
        return True

    print("I couldn't find that application.")
    return False


def open_folder_name(name):

    name = name.lower().strip()

    folder = SPECIAL_FOLDERS.get(name)

    if folder is None:

        print("I don't know that folder.")
        return False

    if not folder.exists():

        print("That folder does not exist.")
        return False

    print("Opening folder:", folder)

    os.startfile(folder)

    return True


def find_file(name):

    name = name.lower().strip()

    search_locations = [
        Path.home() / "Desktop",
        Path.home() / "Documents",
        Path.home() / "Downloads",
        Path("D:/ARVA"),
    ]

    for location in search_locations:

        if not location.exists():
            continue

        for file in location.rglob("*"):

            if file.is_file() and file.name.lower() == name:
                return file

    return None


def open_file(name):

    file = find_file(name)

    if file is None:

        print("I couldn't find that file.")
        return False

    print("Opening file:", file)

    os.startfile(file)

    return True


def close_app(name):

    name = name.lower().strip()

    result = subprocess.run(
        ["taskkill", "/IM", f"{name}.exe", "/F"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"Closed: {name}")
        return True

    print(f"Could not close: {name}")
    return False