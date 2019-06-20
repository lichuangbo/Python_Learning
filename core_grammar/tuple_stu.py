'''
元组：元组可以将多样的对象集合在一起，
    与列表的本质区别在于：元组不可修改
    单个项目组成的元组的写法 ('monkey',)  空元组 ()
'''
zoo = ('Python', 'AJAX', 'Java')
print(type(zoo))
print(len(zoo))
new_zoo = ('monkey', 'rabbit', zoo)     # 元组是可以放不一样的对象的
print(new_zoo)
print(new_zoo[2])
print(new_zoo[2][1])
print(len(new_zoo) - 1 + len(new_zoo[2]))   # 返回元组的全部属性个数
# del(new_zoo[1])  # 报错，‘tuple’ object doesn't support item deletion
# print(new_zoo)

'''
集合：无序的不重复元素的集合，集合可以修改
'''
country = set(['China', 'USA', 'India', 'German'])  # 法一
name_set = {'小明', '小黄', '小王', '小婉', '小明'}     # 法二
print(name_set)     # 输出会直接去除重复的元素
print(type(country))

# 判断元素是否在集合内
print('China' in country)       # True
print('Hongkong' in country)    # False
# 输出顺序随机生成
print(country)
new_country = country.copy()

# 添加新元素
new_country.add('England')

# 判断集合之间的父子关系
print(new_country.issuperset(country))  # True
print(new_country.issubset(country))    # False

# 移除元素
new_country.remove('USA')

# 求集合之间的交集
print(new_country & country)    # 两集合的交集，[China, India, German]

# 清空集合
print("\n", new_country.clear())
print(new_country)


