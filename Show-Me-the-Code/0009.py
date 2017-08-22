from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.hao123.com/")
bs=BeautifulSoup(html,"html.parser")
for link in bs.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
