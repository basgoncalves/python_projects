import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

# find location of current file
# (use 'os.path.dirname(__file__)' if using .py 
# OR 
# 'os.getcwd() ' if using ipynb)
current_script_path = os.path.dirname(__file__)
print(current_script_path)

print("Paste the pubmed URL for the paper: ")
url = input()

try:
    print("requsting data from " + url)
    data = requests.get(url)            # request data
except:
    print(url + ' does not exist')
    url = r'https://pubmed.ncbi.nlm.nih.gov/36457193/'
    print("requsting data from " + url)
    data = requests.get(url)            # request data


filename = os.path.join(current_script_path, '.\\ncbi.html')
with open(filename, 'w+', encoding="utf-8") as f:
    f.write(data.text)


# create data frame
dfs = []

with open(filename, 'r', encoding="utf-8") as f:
    page = f.read()

soup = BeautifulSoup(page, 'html.parser')
authors = soup.findAll('a', class_='full-name')
names = []
for i in range(0,len(authors)):
    names.append(authors[i]['data-ga-label'])

last_name = (names[0].rsplit(" ", 1)[1] + ' et al.')
title = soup.find('h1', class_='heading-title').text.strip()
journal = soup.find('div', class_='journal-actions dropdown-block').button['title']
year = soup.find('span', class_='cit').text[0:4]
doi = soup.find('span', class_='citation-doi').text.strip()

data = {'author': [last_name],'year': [year], 'journal': [journal], 
        'url': [url]}

df = pd.DataFrame(data)
df[0:].to_clipboard(excel=True, sep=None, index=False, header=None)

print({'author':[last_name],'title': [title], 'doi': [doi]})

