import os
from tkinter import filedialog
import tkinter as tk
import re

# Function to find unique file types in a folder
def find_file_types(folder_path):
    file_types = set()
    for root, dirs, files in os.walk(folder_path):
        # Remove hidden items from dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            _, file_ext = os.path.splitext(file)
            file_types.add(file_ext)
    return file_types

# Function to update renaming options based on file types in a folder
def update_renaming_options(folder_path, renaming_options):
    if not folder_path:
        return renaming_options

    file_types = find_file_types(folder_path)
    for file_type in file_types:
        if file_type not in renaming_options.values():
            new_key = "_" + file_type.replace(".", "")
            renaming_options[new_key] = file_type
    return renaming_options

# Function to convert camel case to snake case
def convert_camel_case_to_snake_case(input_string):
    # Use a regular expression to find occurrences of lowercase followed by uppercase
    pattern = re.compile(r'([a-z])([A-Z])')
    
    # Replace occurrences with lowercase followed by underscore and lowercase
    converted_string = re.sub(pattern, r'\1_\2', input_string)
    
    # Convert the entire string to lowercase
    converted_string = converted_string.lower()
    
    return converted_string

#  Function to rename files and folders
def rename_to_lowercase(old_name, renaming_options):
    new_name = convert_camel_case_to_snake_case(old_name)

    # Replace the old file extension with the new file extension
    for old, new in renaming_options.items():
        new_name = new_name.replace(old, new)

    if os.path.exists(new_name): # If the new name already exists
        return

    os.rename(old_name, new_name)

# Function to rename files and folders
def rename_files_and_folders(renaming_options=dict()):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    
    renaming_options = update_renaming_options(folder_path, renaming_options)
    
    if folder_path:
        for root, dirs, files in os.walk(folder_path):
            
            dirs[:] = [d for d in dirs if not d.startswith('.')] # Remove hidden items from dirs
            files = [f for f in files if not f.startswith('.')] # Remove hidden items from files
            
            dirs[:] = [d for d in dirs if not d.startswith('__')] # Remove items starting with '__' from dirs
            files = [f for f in files if not f.startswith('__')] # Remove items starting with '__' from files
                            
            for dir in dirs:
                old_name = os.path.join(root, dir)
                rename_to_lowercase(old_name,renaming_options)
                
            for file in files:
                old_name = os.path.join(root, file)
                rename_to_lowercase(old_name,renaming_options)

if __name__ == "__main__":
    # Function to rename files and folders
    rename_files_and_folders()


# END

