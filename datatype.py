'''
Python 数据类型主要包含
number: int, float, bool, complex
string:
list:
dictionary:
set:
tuple:
'''
# 声明一个变量

first_number = 1        # 整数
print(first_number)
print(type(first_number))   # <class 'int'>

second_number = 3.14    # 浮点数
print(second_number)
print(type(second_number))  # <class 'float'>

third_number = True     # bool数
forth_number = 1 + 3j   # 复数
print(third_number, forth_number)
print(type(third_number), type(forth_number))

str = 'Hello'
str1 = ''' Hello
world!
'''
print(str, type(str))
print(len(str))     # 5
print(str[1])       # e
