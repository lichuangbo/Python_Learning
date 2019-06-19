from threading import Thread
import time

num = 0
num_flag = 1#标识变量，有条件的修改

def add():
    global num
    global num_flag
    if num_flag == 1:
        for i in range(100000):
            num += 1
        num_flag = 0

    print("add------num=%d"%num)

def sub():
    global num
    #线程2通过轮询的方式监视标识变量是否改变
    #不通过加锁的方式来保证线程安全访问变量，通过加条件的方式让线程2一直处于等待状态
    #这种方式虽然也实现了目的，但是效率不高，线程2一直占用着CPU资源
    while True:
        if num_flag != 1:
            for i in range(100000):
                num -= 1
            break


    print("sub------num=%d"%num)

if __name__ == '__main__':
    t1 = Thread(target = add)
    t1.start()

    #多线程同时修改全局变量，数据会出现不可预想的结果，也就是线程不安全
    #time.sleep(2)#确保线程1执行完毕

    t2 = Thread(target = sub)
    t2.start()
    print("final---- num=%d"%num)
