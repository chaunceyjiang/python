import re
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_img_url(URL):#获取正常图片URL列表
    comm=re.compile(r'^http://imgsrc.baidu.com(?:.*?)sign.*')  #过滤非正常图片
    html=urlopen(URL)
    url_list=[]
    bs=BeautifulSoup(html,"html.parser")
    for link in bs.findAll('img'):
        if 'src' in link.attrs:
            url_list+=comm.findall(link.attrs['src'])
    return url_list
def get_img(url_list,save_dir):#下载图片
    index=0
    for url in url_list:
        index+=1
        img=urlopen(url).read()
        with open(save_dir+os.sep+str(index)+'.'+url.split('.')[-1],'wb') as f:
            f.write(img)
if __name__=="__main__":
    URL=r"http://tieba.baidu.com/p/2166231880"
    save_dir=r"C:\Users\chauncey\Desktop"
    os.chdir(save_dir)
    if os.path.exists('imgs') == False:#创建保持目录
        os.mkdir('imgs')
    os.chdir('imgs')
    url_list=get_img_url(URL)
    get_img(url_list,os.getcwd())
