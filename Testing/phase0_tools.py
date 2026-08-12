import os
from pathlib import Path

def open_folder(path):
    path = Path(path)

    if not path.exists():
        print("Path does not exist.")
        return

    if not path.is_dir():
        print("Path is not a folder.")
        return

    os.startfile(path)

#open_folder(r"C:\Users\ARYAN GAVADE\Downloads")
#open_folder(r"C:\ThisFolderDoesNotExist")
#open_folder(r"D:\ARVA\phase0_tools.py")

#---------------------------

def open_file(path):

    path = Path(path)

    if not path.exists():
        print('Error : File does not exists !')
        return

    elif not path.is_file():
        print("Error: Path is not a file!")
        return

    else:
        os.startfile(path)

#open_file(r"D:\ARVA\test.py")
#open_file(r"D:\ARVA\does_not_exist.txt")
open_file(r"D:\ARVA")