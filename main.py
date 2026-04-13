"""
Automatic file organizer script.

This script automates the process of monitoring a directory (such as Downloads)
and organizing incoming files into specific subfolders based on their 
file extensions using pathlib and watchdog.
"""
import shutil
from pathlib import Path

#Supported file extensions and the destination folder for each one
rules = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".mp4": "Video",
    ".avi": "Video",
    ".mkv": "Video",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives"
}
root_dir = Path.home() / "Downloads"

#Iterate only through files, ignoring folders and the script itself
for file in root_dir.iterdir():
    if file == Path(__file__):
        continue
    if not file.is_file():
        continue

    extension = file.suffix.lower() # Standardize to avoid issues with .JPG or .PDF files

    dir_name = rules.get(extension, "Others")

    des_dir = root_dir / dir_name
    des_dir.mkdir(exist_ok=True)# It does not return an error if the folder already exists
    shutil.move(file, des_dir)
    print(f"Move: {file.name} -> {dir_name}")
