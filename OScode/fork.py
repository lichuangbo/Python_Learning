# coding=utf-8

import os
import time

def fork():
    # 在Linux、Unix和mac OS中有fork()方法，可以直接创建一个新的进程，在Windows中不存在
    # 理解：os.fork()会返回两个值，根据返回的PID值来区分父子进程；而且fork()之后的代码两进程都会执行。
    pid = os.fork()
    print(pid)
    # pid<0创建进程失败，pid=0创建子进程，原父进程pid>0
    if pid == 0:
        # getpid()获取当前进程的PID值，getppid获取父进程PID
        # 注意:父进程fork的返回值就是创建出来的子进程的PID
        print("子进程的PID-->%s,父进程的PID-->%s"%(os.getpid(),os.getppid()))
        time.sleep(1)
    else:
        print("父进程的PID-->%s"%os.getpid())
        time.sleep(1)

def varInFork():
    # 注意：在多进程程序中，所有数据都会自己copy一份，进程在自己的数据基础上进行修改
    num = 0
    pid = os.fork()
    if pid == 0:
        num += 1
        print(num)
        time.sleep(1)
    else:
        print(num)
        time.sleep(1)

def multiFork():
    # 多次fork问题，在这个例子中，主进程分叉为一个父进程一个子进程，分别执行第一个if语句；
    # 紧接着，两进程执行完毕if,有各自分叉，得到的父子进程又去执行第二个if语句，所以共有6个进程；
    pid = os.fork()
    if pid == 0:
        print("--1--")
        time.sleep(1)
    else:
        print("--2--")
        time.sleep(1)

    pid = os.fork()
    if pid == 0:
        print("--3--")
        time.sleep(1)
    else:
        print("--4--")
        time.sleep(1)

if __name__ == "__main__":
    #fork()

    #varInFork()
    
    multiFork()


