import requests
from bs4 import BeautifulSoup
import re
from difflib import SequenceMatcher

def get_doi_from_ref_pubmed_with_similarity(ref, similarity_threshold=0.8):
    """
    Attempts to find the DOI of a reference by searching PubMed and comparing
    article titles for similarity.
    """
    title_match = re.search(r'([A-Z].*?)[,.]', ref)
    if not title_match:
        return None
    input_title = title_match.group(1).lower()

    search_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={input_title.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        article_links = soup.find_all('a', class_="docsum-title")
        if not article_links:
            return None

        for link in article_links:
            article_url = "https://pubmed.ncbi.nlm.nih.gov" + link['href']
            article_response = requests.get(article_url, headers=headers, timeout=10)
            article_response.raise_for_status()
            article_soup = BeautifulSoup(article_response.text, 'html.parser')
            article_title_element = article_soup.find('h1', class_='heading-title')
            if article_title_element:
                article_title = article_title_element.text.strip().lower()
                similarity = SequenceMatcher(None, input_title, article_title).ratio()

                if similarity >= similarity_threshold:
                    doi_meta = article_soup.find('meta', attrs={'name': 'citation_doi'})
                    if doi_meta:
                        return doi_meta['content']

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

ref1 = "Aslan, B. G., and Inceoglu, M. M. (2007), A comparative study on neural network based soccer result prediction, Seventh International Conference on Intelligent Systems Design and Applications (ISDA 2007), pp. 545-550, IEEE"
doi1 = get_doi_from_ref_pubmed_with_similarity(ref1)
print(f"DOI 1: {doi1}")

ref2 = "Smith, J., & Doe, A. (2020). The effects of caffeine on cognitive function. Journal of Neuroscience, 40(10), 1234-1245."
doi2 = get_doi_from_ref_pubmed_with_similarity(ref2)
print(f"DOI 2: {doi2}")

ref3 = "Author, A. (2023). Some title. Some Journal. 1(1), 1-10."
doi3 = get_doi_from_ref_pubmed_with_similarity(ref3)
print(f"DOI 3: {doi3}")

ref4 = "A comparative study on neural network based soccer result prediction"
doi4 = get_doi_from_ref_pubmed_with_similarity(ref4)
print(f"DOI 4: {doi4}")