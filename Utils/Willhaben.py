import requests
import os
from bs4 import BeautifulSoup
import pandas as pd


# find location of current file
# (use 'os.path.dirname(__file__)' if using .py
# OR
# 'os.getcwd() ' if using ipynb)


# SELECT CSV FILE PATH AND LOAD DATA
def data_from_willhaben(url):
    try:
        data = requests.get(url)            # request data
    except:
        print("Paste URL for the Willhaben ad (https://www.willhaben.at): ")
        url = input()
        data = requests.get(url)

    current_script_path = os.path.dirname(__file__)

    filename = os.path.join(current_script_path, '.\\ncbi.html')
    with open(filename, 'w+', encoding="utf-8") as f:
        f.write(data.text)

    dfs = [] # create data frame

    with open(filename, 'r', encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, 'html.parser')
    address = soup.find('div', attrs={
                    'data-testid': 'object-location-address'}, class_='Box-sc-wfmb7k-0').text.strip()
    price = soup.find('span', attrs={
                  'data-testid': 'contact-box-price-box-price-value-0'}, class_='Text-sc-10o2fdq-0 iYbzSg').text.strip()
    costs_tree = soup.findAll('span', class_='Text-sc-10o2fdq-0 jfmShM')

    costs = []
    for i in range(0,len(costs_tree)):
        costs.append(costs_tree[i].find('span', class_='Text-sc-10o2fdq-0 gxQSIC').text.strip())
        if i != len(costs_tree)-1:
            costs.append(' + ')
    costs = ' '.join(costs).replace('.',',')

    print('')
    print('')
    print('Data from URL:')
    print('address: ' + address)
    print('price: ' + price)
    print('costs: ' + costs)

    data = {'address': [address],'price': [price], 'costs': [costs], 
        'url': [url]}

    df = pd.DataFrame(data)
    df[0:].to_clipboard(excel=True, sep=None, index=False, header=None)

# test example
# data_from_willhaben('https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zentagasse-zentrumsnahe-45m-altbaumiete-2-liftstock-4-jahre-befristet-studenten-bevorzugt-619573618/')
data_from_willhaben('')


