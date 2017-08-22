from queue import Queue
from threading import Thread,Event
import time
def consumer(out_q):
    while True:
        print("-")
        data,evt=out_q.get()
        evt.set()
        print(data)
        time.sleep(2)
def producer(in_q):
    while True:
        evt=Event()
        print("******")
        in_q.put(("++++",evt))
        evt.wait()
        print('~~~~~')
        time.sleep(2)

q=Queue()
t2=Thread(target=producer,args=(q,))
t1=Thread(target=consumer,args=(q,))

t1.start()
t2.start()
