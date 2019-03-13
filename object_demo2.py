class Father(object):
    name = 'father'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    @classmethod    # 类修饰符，可以用类名直接访问方法，方法中用到的属性必须是类自有的
    def functiona(cls):
        return cls.name

    @property       # 对象可以像访问属性一样访问方法
    def functionb(self):
        return self.age

    # 在继承的基础上可以形成多态
    def printSelf(self):
        print('我是', self.name)


class Son(Father):
    # 方法的重写
    def __init__(self, age, name, sex):
        # super(Son, self).__init__(age, name)      # <法一>
        Father.__init__(self, age, name)            # <法二>
        self.sex = sex

    def printSelf(self):
        print('我是', self.name)


if __name__ == '__main__':
    father1 = Father(27, '小华爸爸')
    print(father1.functionb)
    print(Father.functiona())
    print(father1.printSelf())
    print()
    son1 = Son(10, '小明', 'male')
    print(son1.name, son1.sex, son1.age, end='')
    print(son1.printSelf())
    print('\n子类类型的判断')
    print(isinstance(son1, Father))

