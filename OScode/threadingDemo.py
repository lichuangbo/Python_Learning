from threading import Thread
import time

def sayHello():
    for i in range(5):
        print("Hello")
        time.sleep(1)

# 与进程类似，使用自定义类继承Thread并重写父类run方法
class MyThread(Thread):
    def run(self):
        for i in range(3):
            msg = "My name is" + self.name + "@" + str(i)
            print(msg)
            time.sleep(1)

# 主线程会等待子线程结束，主要是为了回收子线程占用的资源
if __name__ == '__main__':
    t = Thread(target = sayHello)
    t.start()

    t = MyThread()
    t.start()
