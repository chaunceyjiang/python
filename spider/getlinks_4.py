from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bs=BeautifulSoup(html,"html.parser")
    try:
        print(bs.h1.get_text())
        print(bs.find(id="mw-content-text").findAll("p")[0])
        print(bs.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性")
    for link in bs.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage=link.attrs["href"]
                print("---------\n"+newpage)
                pages.add(newpage)
                getLinks(newpage)
getLinks("")