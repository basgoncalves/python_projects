import requests
import os
from bs4 import BeautifulSoup as bs
import pandas as pd
import pygetpapers as pyg
from Bio import Entrez
# test doi 10.1177/0954411913518747

def get_pubmed_link_from_doi(doi):
    Entrez.email = 'basilio.goncalves7@gmail.com'  # Provide your email address
    handle = Entrez.esearch(db='pubmed', term=doi)
    record = Entrez.read(handle)
    handle.close()

    if record['IdList']:
        pubmed_id = record['IdList'][0]
        pubmed_link = f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"
        return pubmed_link

    return pubmed_link

def get_paper_authors_from_ncbi_link(doi):
    current_script_path = os.path.dirname(__file__)# 'os.path.dirname(__file__)' if.py  'os.getcwd() ' if  .ipynb)
    url = get_pubmed_link_from_doi(doi)
    print("requsting data from " + url)
    
    data = requests.get(url)     
    
    ncbi_html = os.path.join(current_script_path, '.\\ncbi.html')
    with open(ncbi_html, 'w+', encoding="utf-8") as f:
        f.write(data.text)

    with open(ncbi_html, 'r', encoding="utf-8") as f:
        page = f.read()

    soup = bs(page, 'html.parser')
    authors = soup.findAll('a', class_='full-name')
    names = []
    for i in range(0,len(authors)):
        names.append(authors[i]['data-ga-label'])

    last_name = (names[0].rsplit(" ", 1)[1] + ' et al.')
    journal = soup.find('div', class_='journal-actions dropdown-block').button['title']
    year = soup.find('span', class_='cit').text[0:4]
    author_string = (last_name + '-' + year + '-' + journal)

    os.remove(ncbi_html)

    return author_string

def get_pdf_from_doi(doi=''):
    
    if not doi:
        print("Paste the DOI of the paper: ")
        doi = input()

    author_string = get_paper_authors_from_ncbi_link(doi)

    url = os.path.join('https://sci-hub.hkvisa.net/',doi)
    
    print(url)
    pdf_filename = author_string.__add__('.pdf')  # Specify the filename for the downloaded PDF
    pdf_filename = 'test.pdf'
    download_path = os.path.join(os.path.expanduser('~'),'AppData\Local\Mendeley Ltd\Mendeley Desktop\Downloaded')
    try:
        os.chdir(download_path)
    except: 
        print(download_path + ' does not exist')
        
    response = requests.get(url)
    if response.status_code == 200:
        with open(pdf_filename, 'wb') as file:
            file.write(response.content)
        print(f"PDF downloaded successfully. Saved as {pdf_filename}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

doi = '10.1177/0954411913518747'
get_pdf_from_doi(doi)



