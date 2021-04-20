#增加--增加指定数据到列表中
#append（）--列表结尾追加数据--列表数据.append（数据）
name_list = ['Tom','Lily','Rose']
name_list.append('xiaoming')  #列表追加数据的时候，直接在原列表里面追加了指定数据，修改了原列表，为可变类型数据
print(name_list)

#如果append追加的是序列，则追加整个序列到列表
name_list = ['Tom','Lily','Rose']
name_list.append(['xiaoming','xiaohong'])
print(name_list)

#extend()--列表结尾追加数据，如果数据是一个序列，则将这个序列逐一添加到列表--列表序列.extend（数据）
name_list = ['Tom','Lily','Rose']
name_list.extend('xiaoming')  #单个数据
print(name_list)

name_list = ['Tom','Lily','Rose']
name_list.extend(['xiaoming','xiaohong'])  #序列数据
print(name_list)

#insert（）--指定位置新增数据--序列列表.insert（下标，数据）
name_list = ['Tom','Lily','Rose']
name_list.insert(1,'xiaoming')
print(name_list)

#删除--del 目标
#删除列表
name_list = ['Tom','Lily','Rose']
del name_list
#print(name_list) --报错了，提示name_list没有定义

#删除指定数据
name_list = ['Tom','Lily','Rose']
del name_list[1]
print(name_list)

#pop()--删除指定下标的数据（默认为最后一个），并返回该数据--列表序列.pop（下标）
name_list = ['Tom','Lily','Rose']
del_name = name_list.pop()
print(del_name)
print(name_list)

#remove()--移除列表中某个数据的第一个匹配项--列表序列.remove（数据）
name_list = ['Tom','Lily','Rose']
name_list.remove('Lily')
print(name_list)

#clear()--清空列表
name_list.clear()
print(name_list)

#修改--修改指定下标数据
name_list = ['Tom','Lily','Rose']
name_list[0] = 'aaa'
print(name_list)

#逆置--reverse（）
num_list = [1,5,2,3,8,5,6]
num_list.reverse()
print(num_list)

#排序--sort（）--列表序列.sort（key = none，reverse = false）--reverse表示排序规则，True代表降序，False代表升序（默认的）
num_list = [1,5,2,3,8,5,6]
num_list.sort(key= None,reverse=True)  #key的用法不清楚
print(num_list)

#复制--copy（）
name_list = ['Tom','Lily','Rose']
name_list1 = name_list.copy()
print(name_list1)