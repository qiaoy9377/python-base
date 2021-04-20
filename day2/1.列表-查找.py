#列表一次性存储多个数据
#1、查找
# 1）下标
name_list = ['Tom','Lily','Rose']
print(name_list[0])
print(name_list[1])
print(name_list[2])

#2）函数
#index()--返回指定数据所在位置的下标--列表序列.index（数据，开始位置下标，结束位置下标）
print(name_list.index('Lily',0,2))
#print(name_list.index('lily'))--查找的数据不存在，报错

#count（）--统计指定数据在当前列表中出现的次数
print(name_list.count('Tom'))

#len()--访问列表长度，即列表中数据的个数
print(len(name_list))

#3)判断是否存在
#in--判断指定数据在某个列表序列，如果在返回True，不存在返回False
print('Lily' in name_list)

print('lily' in name_list)

#not in--判断指定数据不在某个列表序列，如果不在返回True，否则返回False
print('Lily' not in name_list)
print('lily' not in name_list)

#体验：需求--查找用户输入的名字是否已经存在
name = input('请输入您要搜索的名字：')
#判断名字是否在列表中
if (name in name_list):
    #是，提示名字已存在
    print(f'您输入的名字是{name}，名字已存在')
else:
    #否，提示名字不存在
    print(f'您输入的名字是{name}，名字不存在')