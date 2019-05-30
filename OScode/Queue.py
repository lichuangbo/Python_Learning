#coding=utf-8
from multiprocessing import Queue, Process
import os
import time

# 写入数据进程执行代码
def write(q):
    for value in ['A', 'B', 'C']:
        print("put %s to queue"%value)
        q.put(value)
        time.sleep(1)

# 读取数据进程执行代码
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("get %s from queue."%value)
            time.sleep(1)
        else:
            break

if __name__ == "__main__":
    # 主进程创建Queue，传递给子进程pw，pr
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,))
    # 先进行写入，在进行读取
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print("所有数据都已读写完毕")



