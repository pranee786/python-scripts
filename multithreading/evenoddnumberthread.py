from threading import *

class EvenNumbersThread(Thread):
    def run(self):
        for i in range(1,101):
            if i%2 == 0:
                print("Even Number Thread:" + str(i))
                

class OddNumbersThread(Thread):
    def run(self):
        for i in range(1,101):
            if i%2!=0:
                print("Odd Number Thread: " + str(i))


e = EvenNumbersThread()
o = OddNumbersThread()
e.start()
o.start()
for i in range(1,101):
    print('Main Thread: ' + str(i))
