'''
文件操作：
open(’路径名‘, '打开模式')   ’r‘：只读  ’w‘：只写，若文件不存在就新建文件并写入 'r+':读写 'w+'：读写
file.readable()
file.readlines()
file.readline()

'''
file1 = open('D://linkSql.txt', 'r')
print(file1.readable())       # True，可读
# print(file1.readline())     # 返回第一行数据
# print(file1.readlines())    # 返回全部数据
i = 1
for line in file1.readlines():
    print('第{0}行数据：{1}'.format(i, line))
    i += 1
file1.close()

# 写入文件
file2 = open('D://key.key', 'w+')
print(file2.readable())
num = file2.write('\n呵呵,')
file2.write('\n我不认识你')
print(num)
print(file2.readlines())
file2.close()
