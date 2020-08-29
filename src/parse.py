from bs4 import BeautifulSoup, SoupStrainer
import requests

def getLinks(url):
    # returning array
    links = []

    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data)

    for source in soup.find_all('a'):
        links.append(source.get('href'))

    return links