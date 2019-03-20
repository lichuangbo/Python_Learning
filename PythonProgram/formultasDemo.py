# 输入三位数字，返回分离后的各位对应的数字
# while True:
#     number = int(input('Enter an integer:'))
#     if number == 0:
#         break
#     elif number < 100:
#         print('太小')
#         continue
#     elif number > 999:
#         print('too big')
#         continue
#     a = number / 100
#     b = number % 100 / 10
#     c = number % 100 % 10
#     print('a={0},b={1},c={2}'.format(int(a), int(b), int(c)))

# 1-100之间的偶数加法
# sum = 0;
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
#     else:
#         continue
# else:
#     print('1-100的偶数和为{0}'.format(sum))

# 乘法口诀表实现
# for i in range(1, 10):
#     #for j in range(1, 10):     # 代码不够精简，性能低
#     #   if(j <= i):
#     for j in range(1, i+1):
#             print("{0}*{1}={2}\t".format(j, i, i * j), end="")
#     print("")

'''
coding-utf8
一元二次方程的求解计算
ax^2 + b*x + c = 0
m = 0
m > 0
m < 0
'''

import math
import cmath
import unicodedata
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        unicodedata.digit(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


a = input('a = ')
b = input('b = ')
c = input('c = ')
if is_number(a) and is_number(b) and is_number(c):
    a = float(a)
    b = float(b)
    c = float(c)
    m = b ** 2 - 4 * a * c
    if a == 0:
        print('非一元二次方程，有一根 x = {0:0.2f}'.format(- c / b))
    elif a == 0 and b == 0:
        print('方程式不合法')
    elif m == 0:
        x = - b / (2 * a)
        print('二次方程有一根 x = {0:0.2f}'.format(x))
    elif m > 0:
        x1 = (- b + math.sqrt(m)) / (2 * a)
        x2 = (- b - math.sqrt(m)) / (2 * a)
        print('二次方程有两根 x1 = {0:0.2f} x2 = {1:0.2f}'.format(x1, x2))
    else:
        x1 = (- b + cmath.sqrt(m)) / (2 * a)
        x2 = (- b - cmath.sqrt(m)) / (2 * a)
        print('二次方程有两复数根,x1 = {0} x2 = {1}'.format(x1, x2))
else:
    print('请输入正确的数据类型')
