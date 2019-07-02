from multiprocessing import	Pool
import	time, os
# 异步：正在执行着某个任务，并且不确定在什么时候会被打断去执行另外一个任务
# 异步的好处：不用“等待”某个任务的完成，可以先执行其他任务，该任务完成后会通知的，到时才放下其他任务，去执行该任务的后续操作
def	run_func():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(), os.getppid()))
    for i in range(3):
        print('---%d---'%i)
        time.sleep(1)
    # 子进程返回的值，由操作系统转交给了主进程
    return "hahah"

def	callback_func(args):
    print("---callback	func--pid=%d"%os.getpid()) # 父进程进程号
    print("---callback	func--args=%s"%args)

if __name__ == "__main__":
    pool = Pool(3)
    # 以非阻塞的方式向进程池中添加一个进程，执行run_func方法
    pool.apply_async(run_func, callback=callback_func)
    # 主进程休眠，直到子进程执行完了run_func，由操作系统唤醒主进程去执行回调
    # 此处就是一个异步的方式：主进程在休眠中，子进程结束被OS唤醒，主进程放弃休眠去执行回调
    time.sleep(5)
    print("----主进程-pid=%d----"%os.getpid())
