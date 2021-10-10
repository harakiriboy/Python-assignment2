import requests
from bs4 import BeautifulSoup as BS
import newsarticles
from newsarticles import Searcher
from rich import Console

console = Console()
myscrapper = Searcher()

cryptocurrency = input("Input the cryptocurrency you want to see: ")

lists = myscrapper.articleSearcher(cryptocurrency)

num = input("enter num of news you want to see: ")

for i in range(int(num)):
    console.print(lists[i])
    print("-----------------------\n")

print("\nThe number of total website articles is:  " + str(len(lists)))
