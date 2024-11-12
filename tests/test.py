import os
import tkinter as tk
from tkinter import messagebox
import json
import msk_modelling_python.src.mri.test_print_xlsx as print_xlsx

def add_coverage_to_xlsx():
    current_file_path = os.path.dirname(os.path.abspath(__file__))  
    settings_json = os.path.join(current_file_path,"settings.json")

    def save_settings_to_file(settings_json, acetabular_coverage, path_xlsx, sheet_name):
        # Save settings to a JSON file
        settings = {
            "acetabular_coverage": acetabular_coverage.get(),
            "path_xlsx": path_xlsx.get(),
            "sheet_name": sheet_name.get()
        }
        
        with open(settings_json, "w") as file:
            json.dump(settings, file, indent=4)

        messagebox.showinfo("Settings Saved", "Settings have been saved to settings.json")

    def load_settings_from_file(settings_json):
        try:
            with open(settings_json, "r") as file:
                settings = json.load(file)
                return settings
        except FileNotFoundError:
            return None
        
    def on_button_click():
        print_xlsx.add_coverages_to_xlsx(acetabular_coverage.get(),  path_xlsx.get(), sheet_name.get())
        save_settings_to_file(settings_json, acetabular_coverage, path_xlsx, sheet_name)
        root.destroy()  # Close the window

    def create_label_entry(root, text, previous_value=None):
        label = tk.Label(root, text=text)
        label.pack(pady=5)
        entry = tk.Entry(root, width=60)
        entry.pack(pady=5)
        entry.insert(0, previous_value)
        return entry

    def create_button(root, text, command):
        button = tk.Button(root, text=text, command=command)
        button.pack(pady=20)

    # Create the main window
    root = tk.Tk()
    root.title("Simple GUI")
    root.geometry("400x300")  # Set the window size to 400x300

    if load_settings_from_file(settings_json) == None:
        acetabular_coverage = create_label_entry(root, "Enter acetabular_coverage path:")
        path_xlsx = create_label_entry(root, "Enter path for xlsx file:")
        sheet_name = create_label_entry(root, "Enter sheet name:")
    else:
        settings = load_settings_from_file(settings_json)
        acetabular_coverage = create_label_entry(root, "Enter acetabular_coverage path:", settings["acetabular_coverage"])
        path_xlsx = create_label_entry(root, "Enter path for xlsx file:", settings["path_xlsx"])
        sheet_name = create_label_entry(root, "Enter sheet name:", settings["sheet_name"])

    create_button(root, "Run Function", on_button_click)

    # Run the application
    root.mainloop()
    
    
        
if __name__ == "__main__":
    add_coverage_to_xlsx()