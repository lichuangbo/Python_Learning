# coding=utf-8

from multiprocessing import Pool
import time
import os

# 使用进程池的好处
# 1.一入场先将进程池创建完毕，之后的添加任务不用管创建进程这块；只管添加任务就行
# 2.进程当前任务执行完毕，自动去执行另一个任务
# 3.在创建和销毁方面不消耗时间，提高了效率
def funcA(num):
    for i in range(5):
        print("----进程id-->%d, num-->%d"%(os.getpid(),num))
        time.sleep(1)

# 创建一个进程池，最大容量为3个进程
# 
pool = Pool(3)

# 添加10个任务
for i in range(0, 10):
    # 非阻塞方式执行
    #pool.apply_async(funcA,(i,))# 以元组的方式传参
    # 阻塞方式执行
    pool.apply(funcA,(i,))

pool.close() # 关闭进程池，不在添加任务
pool.join() #注意：主进程创建完毕后，不能立马结束，等待进程池完成任务
