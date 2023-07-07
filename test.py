import os
import requests


url = "https://scholar.google.com"


# request data if URL exist / can be open 
try:
    print("requsting data from " + url)
    data = requests.get(url)            
    # Check if the response status code is 200
    if data.status_code == 200:
        print(url + ' does not exist')        
except:
    print('could not request url: ' + url)
    data = []
