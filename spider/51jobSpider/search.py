import requests
from bs4 import BeautifulSoup
import re

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
def searchJob(URL,keyword='Python'):
    data={
    'lang':'c',
    'stype':'2',
    'postchannel':'0000',
    'fromType':'1',
    'line':'',
    'confirmdate':'9',
    'from':'',
    'keywordtype':'2',
    'keyword':keyword,
    'jobarea':'',
    'industrytype':'',
    'funtype':'',
    }
    response=requests.post(url=URL,data=data,headers=headers)
    html=BeautifulSoup(response.content,'lxml')
    return html
def nextHtml(url):
    response=requests.get(url,headers=headers)
    html = BeautifulSoup(response.content, 'lxml')
    return html