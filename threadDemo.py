# import threading
# import time
#
#
# # 使用threading创建线程
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print("退出线程：" + self.name)
#
#
# def print_time(threadName, delay, counter):
#     # 主线程下的子线程会执行5次，Thread1间隔1秒，Thread2间隔2秒，Thread1执行完后自动挂起不会等待Thread2
#     while counter:
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime()))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread1", 1)
# thread2 = myThread(2, "Thread2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()  # 主线程等待子线程执行完在挂起
# thread2.join()
# print("退出主线程")


import threading
import time


'''
使用锁，可以保证数据的同步。当线程要访问资源时，必须先加锁；当要访问的资源被加锁，此线程等待。
threadLock = threading.Lock() 添加锁
acquire() 获得锁
release() 释放锁
'''
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime()))
        counter -= 1


thread1 = myThread(1, "Thread1", 1)
thread2 = myThread(2, "Thread2", 2)

threadLock = threading.Lock()
threads = []

thread1.start()
thread2.start()

# 添加主线程到线程列表
threads.append(thread1)
threads.append(thread2)
print('\n', threads)

# 等待所有线程完成,等价于上段代码
for t in threads:
    t.join()

print("退出主线程")
