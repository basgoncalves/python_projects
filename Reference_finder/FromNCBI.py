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



# find location of current file
current_script_path = os.path.dirname(__file__)# 'os.path.dirname(__file__)' if.py  'os.getcwd() ' if  .ipynb)
print(current_script_path)

print("Paste the pubmed URL for the paper: ")
url = input()

# request data
# if URL doesn't exist use a generic Pubmed link
try:
    print("requsting data from " + url)
    data = requests.get(url)            
except:
    
    print(url + ' does not exist')
    url = r'https://pubmed.ncbi.nlm.nih.gov/36457193/'
    print("requsting data from " + url)
    data = requests.get(url)            

ncbi_html = os.path.join(current_script_path, '.\\ncbi.html')
with open(ncbi_html, 'w+', encoding="utf-8") as f:
    f.write(data.text)

# create data frame
dfs = []
with open(ncbi_html, 'r', encoding="utf-8") as f:
    page = f.read()

os.remove(ncbi_html)

soup = BeautifulSoup(page, 'html.parser')
authors = soup.findAll('a', class_='full-name')
names = []
for i in range(0,len(authors)):
    names.append(authors[i]['data-ga-label'])

last_name = (names[0].rsplit(" ", 1)[1] + ' et al.')
title = soup.find('h1', class_='heading-title').text.strip()
journal = soup.find('div', class_='journal-actions dropdown-block').button['title']
year = soup.find('span', class_='cit').text[0:4]
try:
    doi = soup.find('span', class_='citation-doi').text.strip()
except:
    doi = 'not existent'

data = {'author': [last_name],'year': [year], 'journal': [journal], 
        'url': [url]}

df = pd.DataFrame(data)
df[0:].to_clipboard(excel=True, sep=None, index=False, header=None)

print('')
print('')
print(url)
print({'author':[last_name],'title': [title], 'doi': [doi]})
print(last_name + '-' + year + '-' + journal)


