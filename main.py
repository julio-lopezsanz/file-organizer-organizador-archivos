"""
Automatic file organizer script.

This script automates the process of monitoring a directory (such as Downloads)
and organizing incoming files into specific subfolders based on their 
file extensions using pathlib and watchdog.
"""
import shutil
from pathlib import Path

def get_unique_path(destination, filename):
    """
    If the file already exists at the destination, add a number to the name.
    Otherwise, keep the original name.

    Args:
        destination (Path): target directory for the file
        filename (Path): filename and file extension

    Returns:
        Path: original or modified path if a duplicate exists
    """
    target = destination / filename

    if not target.exists():
        return target # There is no conflict; use the original name

    # Separate the name and extension to insert the number between them
    stem = Path(filename).stem
    suffix = Path(filename).suffix

    counter = 1
    while target.exists():
        new_filename = f"{stem}_{counter}{suffix}"
        target = destination / new_filename
        counter += 1

    return target # Returns the modified filename to avoid conflicts

def organize_file(file):
    """
    Moves a file to the corresponding folder based on its extension.

    Args:
        file (Path): full path of the file to organize
    """

    if file == Path(__file__):
        return
    if not file.is_file():
        return

    extension = file.suffix.lower() # Standardize to avoid issues with .JPG or .PDF files

    # Sort the file by its extension; if no extension is specified, it goes to “Others”
    dir_name = rules.get(extension, "Others")

    des_dir = root_dir / dir_name
    des_dir.mkdir(exist_ok=True)# It does not return an error if the folder already exists

    unique_path = get_unique_path(des_dir, file.name)

    try:
        shutil.move(file, unique_path)
        print(f"Moved: {file.name} -> {des_dir.name}")
    except PermissionError:
        print(f"Permission denied: {file.name} -> skipped")
    except FileNotFoundError:
        print(f"File not found: {file.name} -> skipped")
    except Exception as e:
        print(f"Unexpected error with {file.name}: {e}")

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
for files in root_dir.iterdir():
    organize_file(files)
