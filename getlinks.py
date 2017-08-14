from urllib.request  import urlopen
from bs4 import BeautifulSoup
import re
URL="http://en.wikipedia.org/wiki/Kevin_Bacon"
html=urlopen(URL)
bs=BeautifulSoup(html,"html.parser")
for link in bs.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile(("^(?:/wiki/)((?!:).)*$"))):
    if "href" in link.attrs:
        print(link.attrs["href"])