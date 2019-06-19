def cal_triangle(a, b, c):
    '''三角形面积计算
    海伦计算公式：s(s-a)(s-b)(s-c)/2,其中s=1/2(a+b+c)
    :param a: 边长a
    :param b: 边长b
    :param c: 边长c
    :return: 三角形面积 或者 False
    '''
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        tri_area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return float('%.2f' % tri_area)
    else:
        return False


def is_leap(year):
    '''润年判断情况有二
    1.被400整除
    2.被4整除不能被100整除
    :param year: 输入年分
    :return: 是返回True,否返回False
    '''
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def is_prime(number):
    '''
    质数判断：除1和本身不能被其他数整除
    :param number: 输入任意数
    :return:是返回True,否返回False
    '''
    if number == 1:
        return False
    else:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False
    return True


def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    if n > 2:
        return fib(n - 1) + fib(n - 2)


def cal_fib(n):
    '''
    返回前n个斐波那契数列的值
    第0项是0，第1项是第一个1 从第三项开始，每一项都等于前两项之和  0 1 1 2 3 5 8
    :param n: 前n个
    :return: 数列
    '''
    # fib1 = 0
    # fib2 = 1
    # if n <= 0:
    #     print('error')
    # elif n == 1:
    #     print(fib1)
    # else:
    #     print(fib1, fib2, '', end='')
    #     for i in range(1, n - 1):
    #         fib = fib1 + fib2
    #         fib1 = fib2
    #         fib2 = fib
    #         print(fib, '',  end='')
    # 递归做法
    for i in range(1, n + 1):
        print(fib(i), '', end='')

from math import pow
def is_arm(number):
    '''
    判断是否为阿姆斯特丹数
    n位正整数等于其各位数字的n次方之和 例：153 = 1^3 + 5^3 + 3^3
    :param number:输入任意整数
    :return:返回True/False
    '''
    # 将整数转化为字符串并获取整数位数
    n = len(str(number))
    temp_number = number
    sum_number = 0
    while temp_number > 0:
        remainder = temp_number % 10
        sum_number += pow(remainder, n)
        temp_number //= 10
    if sum_number == number:
        return True
    else:
        return False


print(cal_triangle(3, 4, 5))
print(is_leap(2100))
print(is_prime(11))
cal_fib(10)
print(is_arm(1535))


