'''
字典：由键值对组成，键-不可变对象，唯一  值-随意
        键值对用 ：分割，不同对用 , 分割
'''
sites = {
    'google': 'www.google.com',
    'Youtube': 'www.youtube.com',
    'twitter': 'www.twitter.com',
    3.14: 3.1415926
}
# 输出指定键对应的值
print('The google sites is', sites['google'])
print(type(sites))  # dict
for name, value in sites.items():
    print("{0}'s sites is {1}".format(name, value))

# 添加一键值对属性
sites['linkedin'] = 'www.linkedin.com'

# 删除键即删除值
del(sites['google'])

# 修改值
sites['twitter'] = 'https://www.twitter.com'

# 键是不可以直接修改的，但可以间接改
sites[3] = sites.pop(3.14)

# 输出字典的键和值
print(sites.keys(), sites.values())

'''
列表不可以作为字典中的键
报错： unhashable type: 'list'
而可以存在列表字典
'''
# list1 = [1, 2, 3]
# list2 = ['A', 'B', 'C']
# list3 = ['a', 'b', 'c']
# second_dic = {list1, list2, list3}
# print(second_dic)

# dic1 = {'A': 1, 'B': 2}
# dic2 = {1: 1, 1: 2}
# dic3 = {'a': 1, 'b': 2}
# list_test = [dic1, dic2, dic3]
# print(list_test)        # [{'A': 1, 'B': 2}, {1: 2}, {'a': 1, 'b': 2}]
# print(list_test[0])     # {'A': 1, 'B': 2}
# print(list_test[0]['A'])  # 1
# print('list_test is a {0} and list_test[0] is a {1}'.format(type(list_test), type(list_test[1])))  # list, set
