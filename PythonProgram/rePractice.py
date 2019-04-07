# coding=utf-8
import re
'''
匹配11位电话号码
1开头，35678第二位，之后的0-9随机
^ 开头； $ 结尾； []:从中取一个   {}:数量限定   
'''
# print(re.match(r"1[35678]\d{9}", "183456789118"))   # 12位也匹配
# print(re.match(r"1[35678]\d{9}$", "18345678911"))


'''
提取单词边界信息
\b  提取单词的边界     \B  提取非单词的边界    \s匹配空格
'''
# print(re.match(r"^\w+ve", "hover"))
# print(re.match(r"^\w+ve\b", "hover"))
# print(re.match(r"^\w+\s\bve\b", "ho ve r"))     # \b只负责边界，不负责空格
#
# print(re.match(r"^.+ve\B", "hove r"))   # e右侧必须出现字符
# print(re.match(r"^.+\Bve\B", "hover"))   # ve左右两侧必须有字符


'''
匹配0-100之间的数字  
0 1 2
10 22
100
先不管0和100,[1-9]\d?$匹配1-99，再加上0和100的情况
'''
# print(re.match(r"[1-9]\d?$|0$|100$", '00'))
# print(re.match(r"[1-9]?\d?$|100$"))


'''
从字符串中提取部分信息
从"<h1>标题标签</h1>"中提取段落内容
()可以进行分组， '.'代表任意字符(除\n)，'*'代表0或多个,'.*'代表所有字符 
\num：引用分组num匹配到的字符串，解决网页左右标签一致的情况
(?P<key1>)    给分组正则命名       (?P=key1)   正则使用命名
'''
# result = re.match(r"<h1>(.*)</h1>", "<h1>标题标签</h1>")
# print(result)
# print(result.group(0))   # 匹配全集，相当于group(0)
# print(result.group(1))   # 代表整个正则中第一次提取出的信息
# print(result.groups())   # 将所有匹配的放入元组中
# print(result.groups()[0])

# print(re.match(r"<.+><.+>.+</.+></.+>", "<html><h1>网页段落信息</h1></h>")) # error,
# print(re.match(r"<(.+)><(.+)>.*</\2></\1>", "<html><h1>网页段落信息</h1></html>"))
# print(re.match(r"<(.+)><(.+)>(.*)</\2></\1>", "<div><span>网页段落信息</span></div>").group(3))   # 嵌套标签提取信息
# print(re.match(r"<(?P<key1>.+)><(?P<key2>.+)>(.*)</(?P=key2)></(?P=key1)>", "<div><span>网页段落信息</span></div>"))

'''
sub高级用法:
在原有字符串中值的基础上进行操作，使用方法
例：给学生成绩加10分
'''
# def replace(result):
#     '''
#     匹配几次就调用几次函数
#     :param result: 输入的字符串
#     :return: 处理后结果
#     '''
#     temp = int(result.group()) + 10
#     return str(temp)
# print(re.sub(r'\d+', replace, '小明=70, 小华=75'))


'''
贪婪模式,（正则默认）最大程度地满足自己的
在本例中利用 '\d+' 匹配至少一个数字的特性，贪婪模式就只让分组2匹配1个数字,将数字23匹配到自己里边
在"*","?","+","{m,n}"后⾯加上？，关闭❓前边的贪婪模式。
'''
# print(re.match(r'(.+)(\d+-\d+-\d+-\d+)', "This is a number 234-235-22-423").groups())     # 想要匹配电话，但少了两位
# print(re.match(r'(.+?)(\d+-\d+-\d+-\d+)', "This is a number 234-235-22-423").groups())

# url = """
# <img	data-original="https://rpic.douyucdn.cn/appCovers/2016/1 1/13/1213973_201611131917_small.jpg"	src="https://rpic.douyuc dn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"	st yle="display:	inline;">
# """
# print(re.search(r'https.+?\.jpg', url).group())     # 关闭贪婪模式，提取图片下载地址


notes = """
<div>								
<p>岗位职责：</p> 
<p>完成推荐算法、数据统计、接⼝、后台等服务器端相关⼯作</p> 
<p><br></p> 
<p>必备要求：</p> 
<p>良好的⾃我驱动⼒和职业素养，⼯作积极主动、结果导向</p> 
<p>&nbsp;<br></p> 
<p>技术要求：</p> 
<p>1、⼀年以上	Python	开发经验，掌握⾯向对象分析和设计，了解设计模式</p > 
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p> 
<p>3、掌握关系数据库开发设计，掌握	SQL，熟练使⽤	MySQL/PostgreSQL	中 的⼀种<br></p> 
<p>4、掌握NoSQL、MQ，熟练使⽤对应技术解决⽅案</p>
<p>5、熟悉	Javascript/CSS/HTML5，JQuery、React、Vue.js</p> 
<p>&nbsp;<br></p> 
<p>加分项：</p> 
<p>⼤数据，数理统计，机器学习，sklearn，⾼性能，⼤并发。</p>
</div>
"""
print(re.sub(r'<.+?>', '', notes))      # 提取标签内的内容

sites = """
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""
# print(re.findall(r'http://.+?/', sites))    # 匹配网址
# print(re.sub(r'(http://.+?/)(.*)', lambda x: x.group(1), sites))      # 将网址替换

# hello	world	ha	ha
# print(re.findall(r'\b[a-zA-Z]+\b', 'hello	world	ha	ha'))
