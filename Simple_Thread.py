from threading import Thread
import time

def myloop(name,delay):
        print "Starting " + name
        for i in range(10,1,-1):
                time.sleep(delay)
                print name + " " + str(time.ctime(time.time()))
        print "Ended" + name

def Main():
        t1=Thread(target=myloop,args=("thread1",1))
        t2=Thread(target=myloop,args=("thread2",1))

        t1.start()
        t2.start()


if __name__ == "__main__":
        Main()
