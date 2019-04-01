import re

'''
基本正则表达式复习：
$           ->字符串末尾
^           ->字符串开头
x[abc]y     ->[abc]取一个
x[^abc]y    ->非abc
\d          ->[0-9]
\D          ->[^0-9]
\w          ->[A-Za-z0-9_]
\W          ->非数字字母下划线
\s          ->任意空白字符
\S          ->任意非空字符
[a-z]{4,7}  ->数量词4-7个字母
?           ->零次或一次出现，等价于{0,1}
+           ->一次或多次出现 ，等价于{1,}
*           ->零次或多次出现 ，等价于{0,}
'''

'''
1.re.match(正则[pattern], 字符串[string], 标志位[flags=0])
从字符串起始位置匹配，不是起始位置，返回none；是，返回match对象。不常用
'''
print(re.match('www', 'www.runoob.com'))
print(re.match('con', 'www.runoob.com'))

'''
2.re.search(pattern, string, flags=0)
扫描整个字符串并返回第一次匹配的，比match()常用
'''
search = re.search(r'www.*', 'www.runoob.com')
if search:  # 此时可以理解为对象存在
    print('www成功匹配')
    print(search.group(0))  # group(0)返回的是完整的元组
elif re.search('com', 'www.runoob.com').span():
    print('com成功匹配')

'''
3.re.findall(pattern, string[, flags])
在字符串中找到正则匹配的所有子串，并返回一个列表，没有找到匹配返回空列表
'''
print(re.findall(r'www.*', 'www.runoob.com'))   # 以列表的形式返回
print(re.findall(r'[A-Z]', 'Hello World'))
print(re.findall(r'[\d]', '15503609389@163.com'))
print(re.findall(r'[a-z]{3,4}', 'java*&39android##@@python'))

'''
4. re.sub(pattern, 替换[repl], 原始[string], count=0)
替换字符串（常用来去空格，替换间隔符）
'''
print(re.sub(r' ', '', '1 + 2 = 3'))
print(re.sub(r'-', '', "2004-959-559 # 这是一个电话号码"))
print(re.sub(r'#', '%', '#123#23', 1))  # 替换第一个#

'''
5.re.compile(pattern[, flags])
编译正则表达式，生成一个正则表达式Pattern对象，为match和search服务 
'''
pattern1 = re.compile(r'\d+')
print(pattern1.match('one12twothree34four'))    # 查找头部
print(pattern1.match('one12twothree34four', 3, 10).span())  # 指定位置查询
print(pattern1.match('one12twothree34four', 3, 10).group(0))

print(pattern1.search('one12twothree34four').group(0))
'''
6.re.split(pattern, string[, maxsplit=0, flags=0])
按照能够匹配的子串将字符串分割后返回列表
'''
print(re.split('\W+', 'twitter, google, youtube, _, 123'))  # 以列表形式返回
print(re.split('\W+', 'twitter, google, youtube, _, 123', 1))  # 限制分割次数，默认0无限分
