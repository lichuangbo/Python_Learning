import threading
# 创建全局Threadlocal
# Threadlocal相当于为每个线程，copy了一个副本，并在此副本的基础上读写
# 很好的解决了参数在⼀个线程中各个函数之间互相传递的问题
local_school = threading.local()

def process_student():
    #获取当前线程关联的学生
    std = local_school.student
    print('hello, %s (in %s)'%(std, threading.current_thread().name))

def process_thread(name):
    # 将传递的参数赋值给变量
    # 注意：虽然local_school是全局变量，但是local_school.student却是一个局部变量互不影响
    local_school.student = name
    process_student()

# 创建两个子线程，分别传参 'xiaowang' 和 'xiaotian'并指定了线程名字
t1 = threading.Thread(target=process_thread, args=('xiaowang',), name='Thread-1')
t2 = threading.Thread(target=process_thread, args=('xiaotian',), name='Thread-2')
t1.start()
t2.start()

