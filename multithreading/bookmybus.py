from threading import *

class BookMyBus:
    def __init__(self,avaiableSeats):
        self.avaiableSeats = avaiableSeats
        #self.l = Lock()
        self.l = Semaphore()

    def buy(self,seatsRequested):
        self.l.acquire()
        print('Total seats avaiable: ',self.avaiableSeats)
        if(self.avaiableSeats >= seatsRequested):
            print('Confirming a seat')
            print('Processing the payment')
            print('Printing the Ticket')
            self.avaiableSeats -= seatsRequested
            print('Seats booked for Thread: ',current_thread().getName())
        else:
            print('Sorry, No seats are avaiable to book for Thread',current_thread().getName())
        self.l.release()


obj = BookMyBus(10)
t1 = Thread(target=obj.buy,args=(10,))
t2 = Thread(target=obj.buy,args=(6,))
t3 = Thread(target=obj.buy,args=(1,))
t1.start()
t2.start()
t3.start()
