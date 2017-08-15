from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import re
conn=pymysql.connect(host='192.168.174.131',port=3307,user='root',passwd='123456',db='wikipedia',charset='utf8')
cur=conn.cursor()
cur.execute("show tables;")
print(cur.fetchall())
def insertPageNotExists(url):
    cur.execute("select * from pages where url = '"+url+"';")
    if cur.rowcount==0:
        cur.execute("insert into pages(url) values(%s);",(url))
        conn.commit()
        return cur.lastrowid
    else:
        cur.fetchone()[0]
def insertLink(fromPageID,toPageId):
    cur.execute("select * from links where fromPageId=%s and toPageId=%s",(int(fromPageID),int(toPageId)))
    if cur.rowcount==0:
        cur.execute("insert into links(fromPageId,toPageId) values(%s,%s)",(int(fromPageID),int(toPageId)))
        conn.commit()
pages=set()

def getLinks(pageUrl,recursionLevel):
    global pages
    if recursionLevel>4:
        return
    pageId=insertPageNotExists(pageUrl)
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bs=BeautifulSoup(html,"html.parser")
    for link in bs.findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId,insertPageNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            newpage=link.attrs['href']
            pages.add(newpage)
            getLinks(newpage,recursionLevel+1)
getLinks("/wiki/Kevin_Bacon",0)
cur.close()
conn.close()
