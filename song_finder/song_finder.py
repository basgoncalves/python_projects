import requests, os, sys
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from distutils.log import error

def get_year_range():
    current_year = date.today().year

    print('Please input values to help scrape data \n \n')
    start = int(input("Type the starting year:"))
    end = int(input("Type final year:"))

    if start < 1948:
        start = 1948

    if end > current_year:
        end = current_year

    if start > end and start != end:
        error('start year cannot be after the final year') 

    years = list(range(start,end+1))
    return years

use_default_settings = input("Do you want to use the deadult settings (Y/N)? ")

if use_default_settings == 'N':
    searchfor = input("Type stirngs to find in the songs separated by ',' ")
    years = get_year_range()
else:
    searchfor = ['super','con','com']
    years = list(range(2000,2016))

main_dir = os.path.dirname(__file__) # change for os.path.dirname(__file__)  if using .py file
html_folder = (main_dir + '\\html')

if os.path.isdir(html_folder):[]
else:os.mkdir(html_folder)

url_general = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{}'

print('checking the statuts of ' + url_general.format(years[0]))
response = requests.get(url = url_general.format(years[0]))                 # check if the state of first url to ensure the 
print('status: ' + response.reason)

if response.reason == 'Not Found':
    sys.exit('check the url_general ')

# import html files
print('importing html files...')
for year in years:
    url = url_general.format(year)
    data = requests.get(url)                                               # request url per year 
    filename = (html_folder + '\\{}.html'.format(year))
    with open(filename,'w+', encoding="utf-8") as f:                        
        f.write(data.text)                                                  # write html file
print('html files imported to ' + html_folder)

# create data frame
print('creating data frame with songs...')
list_songs =[]
for year in years:

    filename = (html_folder + '\\{}.html'.format(year))
    with open(filename,'r',encoding="utf-8") as f:
        page = f.read()
        soup = BeautifulSoup(page,'html.parser')
        all_songs = soup.find_all(class_='wikitable sortable')              # find the elemnst in the HTML in the wikitable
        all_songs = pd.read_html(str(all_songs))                            # read HTML to dataframe
        all_songs = pd.DataFrame(all_songs[0])                              
        all_songs['Year'] = year                                            # add the year column
        list_songs.append(all_songs)                                        # append to the list of songs

all_songs = pd.concat(list_songs)                                           # convet list to df
all_songs = all_songs.drop(columns=['No.','№'])                             # revome the Number comuns (there are two)
print('table with songs created')

csv_filename = (main_dir + '\\song_table.csv')                              # save as csv 
all_songs.to_csv(csv_filename)
print('songs.csv file saved')

filename = (main_dir + '\\song_table.csv')                                  
all_songs = pd.read_csv(filename)

selected_songs = all_songs[                                                 # select songs that contain the strings input by the user
    all_songs['Title'].str.contains('|'.join(searchfor), 
    case=False)]

selected_songs.to_csv((main_dir + '\\selected_songs.csv'))                  # save selected songs as csv

print('\n \n selected songs: \n ')
print(selected_songs.Title)
print('Seecting song that contain ' + '|'.join(searchfor))
