from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,random,datetime
random.seed(datetime.datetime.now())

def getLinks(articleURL):
    html=urlopen("http://en.wikipedia.org"+articleURL)
    bs=BeautifulSoup(html,"html.parser")
    return bs.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile(("^(?:/wiki/)((?!:).)*$")))
links=getLinks("/wiki/William_Adama")
print(len(links))
print(type(links))
while len(links) >0 :
    newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links=getLinks(newArticle)