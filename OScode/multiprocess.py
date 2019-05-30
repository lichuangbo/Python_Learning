# coding=utf-8

from multiprocessing import Process
import time

def run_func():
    for i in range(5):
        print("---111111---")
        time.sleep(1)

# 使用Process的子类的方法创建进程
class MyProcess(Process):
    # 重写Process类的run方法
    def run(self):
        print("----22222---")
        time.sleep(1)

if __name__ == "__main__":
    # 因为fork不能在Windows中运行，所以使用专门的平台Process
    # 与fork不同的是，主进程会等待process创建的子进程;fork不会等待
    p = Process(target = run_func)
    p.start()
    # join()等待其他进程执行完毕，[timeout]最大时间限度
    p.join()
    print("the end")

    p1 = MyProcess()
    p1.start()
