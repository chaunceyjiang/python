import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
url='http://jobs.51job.com/beijing-cyq/86997597.html?s=01&t=0'

response=requests.get(url,headers=headers)
html=BeautifulSoup(response.content,'lxml')
s=''
for string in html.find('div',{'class':'bmsg job_msg inbox'}).stripped_strings:
    s+=repr(string)+'\n'
position=str(html.find('div',attrs={'class':'bmsg job_msg inbox'}).span.get_text()).strip('\r\t\n ')
print(s,position[:-1])