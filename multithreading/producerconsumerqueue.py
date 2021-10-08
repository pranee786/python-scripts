import queue
import random
from time import sleep
from threading import *

def producer(q):
    while True:
        print('Producing')
        q.put(random.randint(1,50))
        print('Produced')
        sleep(3)

def consumer(q):
    while True:
        print('Ready to Consuming')
        print('Consumed data: ',q.get())
        sleep(3)

q = queue.Queue()
t1 = Thread(target=consumer,args=(q,))
t2 = Thread(target=producer,args=(q,))
t1.start()
t2.start()
