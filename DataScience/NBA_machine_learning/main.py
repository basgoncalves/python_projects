import requests 
import os
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# define directory and years to use
cwd = os.getcwd() # change for '__file__' if using .py 
years = list(range(1991,2023))

# import data (skip if it has been done)
url_general = "https://www.basketball-reference.com/awards/awards_{}.html"

for year in years:
    url = url_general.format(year)
    data = requests.get(url)

    filename = os.path.join(cwd, '.\\results\\{}.html'.format(year))
    # filename = os.path.join('results\{}.html'.format(year))
    with open(filename,'w+', encoding="utf-8") as f:
        f.write(data.text)
     

# create data frame for MVPs
dfs =[]
mvp_folder = (cwd + '\\mvps')
if os.path.isdir(mvp_folder):
     []
else:
     os.mkdir(mvp_folder)

for year in years:

    filename = (mvp_folder + '\\{}.html'.format(year))
    with open(filename,'r',encoding="utf-8") as f:
        page = f.read()

        soup = BeautifulSoup(page,'html.parser')
        soup.find('tr', class_='over_header').decompose()
        mvp_table = soup.find_all(id='all_mvp')
        mvp_season = pd.read_html(str(mvp_table))[0]    # without the [0] mvp_season is a list and not table 
        mvp_season['Year'] = year                       # add a column called year

        dfs.append(mvp_season)  

mvps = pd.concat(dfs)

filename = (cwd + '\\mvps.csv')
mvps.to_csv(filename)
mvps.head(3) #first N rows
mvps.tail(2)  #last N rows