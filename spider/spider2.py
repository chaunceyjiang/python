from bs4 import BeautifulSoup
import requests
from selenium import webdriver
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'home.51cto.com',
    'Referer':'http://home.51cto.com/index',
    'Proxy-Connection':'keep-alive'
    }



url="http://home.51cto.com/index"

session=requests.Session()
response=session.get(url,headers=headers)
print(session.cookies)
bs=BeautifulSoup(response.content,"html.parser")
csrf=bs.find("input",attrs={"name":"_csrf"}).get("value")
print(csrf+"\n")
data={
        '_csrf':csrf,
	'LoginForm[username]':"xxxxxxx",
	'LoginForm[password]':"xxxxxxx",
	'LoginForm[rememberMe]':'0',
	'login-button':'登 录'
        }


session.post(url,data=data,headers=headers)

response=session.get("http://down.51cto.com/credits")
#driver=webdriver.Chrome(r"C:\Python\phantomjs\bin\chromedriver.exe")
#driver.get("http://down.51cto.com/credits")
bs=BeautifulSoup(response.content,"html.parser")
print(bs)
