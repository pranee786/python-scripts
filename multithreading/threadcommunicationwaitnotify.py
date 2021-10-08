from threading import *
from time import sleep

class Producer:
    def __init__(self):
        self.productsList = []
        self.c = Condition()

    def produce(self):
        self.c.acquire()
        for i in range(1,5):
            self.productsList.append("Product " + str(i))
            sleep(1)
            print("Product Added")
        self.c.notify()
        self.c.release()

class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0) # No waiting once producer is notified since timeout = 0seconds
        self.prod.c.release()
        print("Orders Processed " , self.prod.productsList)

p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
