from threading import Thread, Lock
import time

num = 0

def add():
    global num
    # 锁的使用，访问前先加锁，访问后释放掉锁；而且当添加了锁之后，其他线程不能添加锁，只能等待它释放掉锁
    for i in range(100000):
        mutex.acquire()
        num += 1
        mutex.release()
    print("add------num=%d"%num)

def sub():
    global num
    # 使用通知机制代替轮询，减轻CPU的负担
    # 加锁位置：要加在最关键的代码上,也就是加锁阶段越少越好，主要是为了提升多线程的工作性能
    #mutex.acquire()
    for i in range(100000):
        mutex.acquire()
        num -= 1
        mutex.release()
    #mutex.release()
    print("sub------num=%d"%num)

if __name__ == '__main__':
    #使用同步的方法处理线程安全问题，效率更高：线程1在执行过程中，线程2处于阻塞状态，不占用CPU资源
    mutex = Lock()#创建锁，默认打开状态
    t1 = Thread(target = add)
    t1.start()

    t2 = Thread(target = sub)
    t2.start()
    print("final---- num=%d"%num)
