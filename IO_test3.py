# import pickle
# shoplistfile = 'D:\\shoplist.data'
# shoplist = ['apple', 'banana', 'mango']
# # 以二进制格式打开一个文件执行写入操作
# f = open(shoplistfile, 'wb')
# # 把对象存储到文件中
# pickle.dump(shoplist, f)
# f.close()
# del shoplist
#
# f = open(shoplistfile, 'rb')
# storedlist = pickle.load(f)
# print(storedlist)

'''
except异常 可以放在一个元组中，如：except (RuntimeError, NameError, ValueError) pass
异常处理可以加else语句，但必须放在所有的except后面，指的是 没有异常时执行else语句
raise抛出异常(必须是异常的实例或者是异常类)，不处理
'''
try:
    print(2 * i)
    print(2 + '2')
    print(1 / 0)
except ZeroDivisionError:
    print('除数不可为0')
except TypeError:
    print('输入类型有误')
except NameError:
    print('未定义变量')
except:
    print('Unexpected error')
    raise
else:
    print('succeed')

# 抛出异常
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)
raise MyError('error')

# 可应用于对数据输入的判断，ValueError：字母、数字等字符串，小数
# while True:
#     try:
#         int_type_number = int(input('Enter a number here:'))
#         print('输入正确')
#     except ValueError:
#         print('Try again')
