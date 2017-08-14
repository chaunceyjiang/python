from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages=set()

def getLinks(articleURL):
    html=urlopen("http://en.wikipedia.org"+articleURL)
    bs=BeautifulSoup(html,"html.parser")
    for link in bs.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile(("^(?:/wiki/)((?!:).)*$"))):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                print("New page! "+link.attrs["href"])
                pages.add(link.attrs["href"])
                getLinks(link.attrs["href"])
getLinks("/wiki/Kevin_Bacon")
