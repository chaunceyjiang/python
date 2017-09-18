from search import *
from htmlParser import *
from threading import Thread
from queue import Queue
import pymongo
import time
postUrl='http://search.51job.com/jobsearch/search_result.php'
keyword='Python'

q=Queue(500)
html=searchJob(postUrl,keyword)
all_url_list=fetch_all_Url(html)
threads=[]
threads2=[]
client=pymongo.MongoClient('192.168.174.131',27017)
db=client['51job']
info_tables=db['info_tables_'+keyword]
signal=True
def save2mongo(q):
    while signal:
        info=q.get()
        info_tables.insert_one(info).inserted_id
while len(all_url_list)!=0:
    if len(threads) < 100:
        url=all_url_list.pop()
        t1=Thread(target=evert_last_Url,args=(url,q))
        t1.start()
        threads.append(t1)
    for t in threads:
        if t.is_alive()==False:
            threads.remove(t)
    if len(threads2) <5:
        t2 = Thread(target=save2mongo, args=(q,))
        t2.start()
        threads2.append(t2)

for t in threads:
    t.join()
while q.empty() != True:print(q.qsize())
signal=False
print('here')
for t in threads2:
    t.join()
