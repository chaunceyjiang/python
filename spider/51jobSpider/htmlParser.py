import requests
from bs4 import BeautifulSoup
import re
from search import *

def fetch_all_Url(html):
    url_list=[]
    try:
        total = html.find('div', attrs={'class': 'p_in'}).contents[-4].get_text()
        match = int(re.findall(r'\d+', total)[0])
        link = html.find('div',attrs={'class':'p_in'}).find('ul').contents[-2]
        url_list.append(link.a['href'])
    except :
        pass
    else:
        full=url_list[0].split('.')
        tmp=full[-2]
        tmp = tmp.split(',')[0:-1]
        s=','.join(tmp)
        for i in range(1,match):
            full.pop(-2)
            x=s+','+str(i)
            full.insert(-1,x)
            url_list.append('.'.join(full))
    return url_list[1:]
def get_detailed_information(info):
    html=nextHtml(info['详细信息URL'])
    position=str(html.find('div',attrs={'class':'bmsg job_msg inbox'}).span.get_text()).strip()
    
def evert_last_Url(url,q):
    html=nextHtml(url)
    for el in html.find('div',attrs={'id':'resultList'}).findAll('div',attrs={'class':'el'}):
        info = {}
        try:
            info['招聘职位']=str(el.contents[1].span.a.get_text()).strip()
            info['详细信息URL']=str(el.contents[1].span.a['href']).strip()
            info['公司名称']=str(el.contents[3].a['title']).strip()
            info['公司全部招聘信息URL']=str(el.contents[3].a['href']).strip()
            info['公司地址']=str(el.contents[5].get_text())
            info['薪资范围']=str(el.contents[7].get_text())
            info['招聘日期']=str(el.contents[9].get_text())
        except :
            pass
        else:
            get_detailed_information(info)
#            q.put(info)
