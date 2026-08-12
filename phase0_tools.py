import os
from pathlib import Path

def open_folder(path):
    path = Path(path)

    if path.exists():
        os.startfile(path)
    else:
        print("Folder does not exist.")


open_folder(r"C:\Users\ARYAN GAVADE\Downloads")