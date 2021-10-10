import requests
from bs4 import BeautifulSoup as BS

from os import readlink
import webbrowser

class Searcher():
    def articleSearcher(self, cryptocurrency):
        
        url = "https://www.google.com/search?q=site%3Acoinmarketcap.com+alexandria+" + cryptocurrency
        
        myrequest = requests.get(url)
        
        soup = BS(myrequest.content, 'html.parser')
        
        Linkslist = []

        for link in soup.find_all('a'):
            href = link.get('href')
            if "https://coinmarketcap.com/" in href:
                Link = "https://www.google.com"+href
                Linkslist.append(Link)
        return Linkslist

