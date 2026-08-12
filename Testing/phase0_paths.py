from pathlib import Path

home = Path.home()

downloads = home / "Downloads"
documents = home / "Documents"


print(downloads.exists())
print(downloads.is_dir())
print(downloads.is_file())

print(downloads)
print(documents)
print('-------------------------------')
import os

print(os.environ["USERNAME"])
#print(os.environ["PATH"])

# -> where.exe notepad
print('-------------------------------')

import shutil

print("Home:", Path.home())

print("Username:", os.environ["USERNAME"])

print("\nNotepad:")
print(shutil.which("notepad.exe"))

print("\nPython:")
print(shutil.which("python"))

print("\nChrome:")
print(shutil.which("chrome"))