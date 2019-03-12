'''
Python对象：
对象名大写   类前要有两行空行    类内函数前要有一行
类的方法和函数的区别 ：方法中都有self实例
默认公有属性， 私有属性(变量和方法)的写法：__private_attrs
调用私有属性时，用self.__** ,在类外不可以直接访问
Python允许多继承
'''


class FirstObject:
    i = 1           # 共有属性
    __count = 0     # 私有属性

    # 定义构造和析构函数，具体如下
    def __init__(self, i):
        self.i = i

    def __del__(self):
        print('Object is being deleted')

    def sayhello(self):
        print('hello')
        print(self)
        print('调用私有属性', self.__count)


class Student:
    age = 21
    name = ''
    sex = 'male'

    # self此处可以理解为this
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


# 单继承
class Master(Student):
    salary = 1500

    def __init__(self, name, sex, salary):
        Student.__init__(self, name, sex)
        self.salary = salary

    def introduct(self):
        print('\nMy name is {0}, sex {1} and salary is {2}'.format(self.name, self.sex, self.salary))


# 多继承实例
class FirstStudent(FirstObject, Student):
    def __init__(self, name, sex, i):
        Student.__init__(self, name, sex)
        FirstObject.__init__(self, i)


# 实例化对象
object1 = FirstObject(2)     # Hi
print(object1)      # 返回在计算机中的内存地址，<__main__.FirstObject object at 0x0000012CA2033EB8>
print(type(object1))  # <class '__main__.FirstObject'>
object1.sayhello()
del object1         # Object is being deleted

object2 = Student('xiaotian', 'male')
print(object2.name, object2.sex, end='')

object3 = Master('xiaowang', 'female', 2900)
object3.introduct()

object4 = FirstStudent('xiaoGang', 'male', 2)
