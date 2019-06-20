# 列表
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), ' item to purchase.')
for item in shoplist:
    print(item, " ")

# 添加列表项
shoplist.append('rice')
print('My shopping list is now', shoplist)

# 列表项排序
shoplist.sort()
print('Sorted shopping list is', shoplist)

# 查找列表项
print('The first item I will buy is', shoplist[0])

olditem = shoplist[0]
# 删除列表项
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

# 嵌套列表
mylist = [['apple', 'mango', 'rice'], ['12', '14', '45']]
print(mylist[0][1])     # 访问apple

# 移除列表中的索引对应的项, 并返回至当前的变量
del_list = mylist.pop(1)
print(del_list)
print(mylist)

# 移除指定列表项, 不会返回
del_list.remove('12')
print(del_list)
