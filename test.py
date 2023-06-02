import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
    

def save_to_xlsx():
    
    # Step 1: Load the .xlsx file
    file_path = askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

    # Check if a file was selected
    if not file_path:
        messagebox.showinfo("Info", "No file selected. Exiting...")
        exit()

    # Step 2: Find all the tabs and ask the user to select one
    xl = pd.ExcelFile(file_path)
    tabs = xl.sheet_names()
    selected_tab = messagebox.askquestion("Select Tab", "Select a tab to add a row:", choices=tabs)

    # Check if a tab was selected
    if selected_tab == 'no':
        messagebox.showinfo("Info", "No tab selected. Exiting...")
        exit()

    # Step 3: Add a row to the selected tab
    df = pd.read_excel(file_path, sheet_name=selected_tab)
    new_row = pd.DataFrame({'Column1': 'Value1', 'Column2': 'Value2'}, index=[0])
    df = pd.concat([df, new_row])

    # Step 4: Save the .xlsx file
    xl_writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    df.to_excel(xl_writer, sheet_name=selected_tab, index=False)
    xl_writer.save()

    # Step 5: Open the file in the system viewer
    os.startfile(file_path)

save_to_xlsx()