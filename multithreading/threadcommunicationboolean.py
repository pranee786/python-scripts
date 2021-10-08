from threading import *
from time import sleep

class Producer:
    def __init__(self):
        self.productsList = []
        self.ordersPlaced = False

    def produce(self):
        for i in range(1,5):
            self.productsList.append("Product " + str(i))
            sleep(1)
            print("Product Added")
        self.ordersPlaced = True

class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        while self.prod.ordersPlaced == False:
            sleep(0.2)
            print("Waiting for the orders")

        print("Orders Processed " , self.prod.productsList)

p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
