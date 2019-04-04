from queue import Queue
from threading import Thread, Event
'''
多个不同的线程之间会存在通信
线程间通信实际上是在线程间传递对象引用，可以使用queue库中的队列实现， 也可以使用Condition变量封装自己定义的数据结构

'''
# 结束标志
_sentinel = object()


def write(q):
    '''
    1. get() 和 put() 方法都支持非阻塞方式和设定超时   q.get(block=False)
    可以用来发生无限阻塞的情况
    2. 超时自动终止以便检查终止标志，使用 q.get() 的可选参数 timeout  q.get(timeout=5.0)
    '''
    # 写数据进程
    for value in ['aaa', 'bbb', 'ccc']:
        print('写进 Queue 的值为：{0}'.format(value))

        # q.put(value)
        # q.put(_sentinel)

        # 需要在read时读取一个数据能立刻得到通知，可以在发送的同时加入事件；此后就可以通过事件来监听
        evt = Event()
        q.put((value, evt))



def read(q):
    # 读取数据进程
    while True:
        value, evt = q.get()
        print('从 Queue 读取的值为：{0}'.format(value))
        evt.set()
        print(evt)

        # 当读到结束标志(一个特殊的数据：在write操作时放入)时，关闭线程。解决一些不必要的麻烦
        # if value is _sentinel:
        #     break


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=write, args=(q,))
    t2 = Thread(target=read, args=(q,))
    t1.start()
    t2.start()
