import os
from tkinter import filedialog
import tkinter as tk
import re
import os
from tkinter import filedialog
import tkinter as tk

def rename_files_and_folders(renaming_options):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                old_name = os.path.join(root, file)
                file_name, file_ext = os.path.splitext(file)
                words = re.findall(r'\w+', file_name)
                new_name = os.path.join(root, '_'.join(word.lower() if word.isalpha() else word for word in words) + file_ext)
                for old, new in renaming_options.items():
                    new_name = new_name.replace(old, new)
                os.rename(old_name, new_name)
            for dir in dirs:
                old_name = os.path.join(root, dir)
                words = re.findall(r'\w+', dir)
                new_name = os.path.join(root, '_'.join(word.lower() if word.isalpha() else word for word in words))
                for old, new in renaming_options.items():
                    new_name = new_name.replace(old, new)
                os.rename(old_name, new_name)


def find_file_types(folder_path):
    file_types = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            _, file_ext = os.path.splitext(file)
            file_types.add(file_ext)
    return file_types

def update_renaming_options(renaming_options):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return renaming_options

    def find_file_types(folder_path):
        file_types = set()
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                _, file_ext = os.path.splitext(file)
                file_types.add(file_ext)
        return file_types

    file_types = find_file_types(folder_path)
    for file_type in file_types:
        if file_type not in renaming_options.values():
            new_key = "_" + file_type.replace(".", "")
            renaming_options[new_key] = file_type
    return renaming_options

renaming_options = {
    "_osim": ".osim",
    "_jpg": ".jpg",
    "_stl": ".stl",
    "_vtp": ".vtp",
    "_obj": ".obj",
    "_mtl": ".mtl",
    "_dae": ".dae",
    "_fbx": ".fbx",
    "_blend": ".blend",
}

renaming_options = update_renaming_options(renaming_options)

print(renaming_options)

rename_files_and_folders(renaming_options)


