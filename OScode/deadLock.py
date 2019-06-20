#coding=utf-8
import	threading 
import	time

class MyThread1(threading.Thread):				
    def	run(self):								
        if mutexA.acquire():
            print(self.name+'----do1---up----')
            time.sleep(1)
            #发生死锁，线程1等待线程2对锁的释放，同时线程2也在等待线程1对锁的释放，
            if mutexB.acquire(1):
                print(self.name+'----do1---down----')
                mutexB.release()
            mutexA.release()

class MyThread2(threading.Thread):
    def	run(self):
        if mutexB.acquire():
            print(self.name+'----do2---up----')
            time.sleep(1)
            if mutexA.acquire(1):
                print(self.name+'----do2---down----')
                mutexA.release()
            mutexB.release()

if  __name__ ==	'__main__':
    mutexA = threading.Lock()
    mutexB = threading.Lock()
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()	
    t2.start()
