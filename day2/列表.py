list1 = []
list2 = list()

name_list = ['Tom','Lily','Rose','Tom']
#下标查找
print(name_list[0])
print(name_list[1])
print(name_list[2])
#函数查找
#index()
print(name_list.index('Lily',0,2))
#print(name_list.index('tom')) #没找到报错了

#count（）
print(name_list.count('Tom'))
print(name_list.count('lily'))  #返回0

#len（）
print(len(name_list))

#判断-in 、not in
print('Lily'in name_list)
print('lily' in name_list)
print('Lily' not in name_list)
print('lily' not in name_list)

# #体验
# name = input('请输入您要查找的名字：')
# if name in name_list:
#     print(f'您输入的名字是{name}，名字已存在')
# else:
#     print(f'您输入的名字是{name}，名字不存在')

#增加
#append（）
name_list.append('xiaoming')
print(name_list)

name_list.append(['小米','小红'])
print(name_list)

#extend（）
name_list.extend('xiao')
print(name_list)

name_list.extend(['xiaohong','xiaoming'])
print(name_list)

#insert()
name_list.insert(2,'张三')
print(name_list)

#删除--del（）
# del name_list
# print(name_list)  #被删除了会报错，提示没有定义
#按照下标删除
del name_list[6]
print(name_list)
#pop（）
del_name = name_list.pop()
print(del_name)
print(name_list)

del_name2 = name_list.pop(-3)
print(del_name2)
print(name_list)

#remove（）--移除第一个匹配项
name_list.remove('Tom')
print(name_list)

#clear()--清空列表
name_list.clear()
print(name_list)

#修改
#按照下标修改数据
name_list = ['Tom','Lily','Rose','Tom']
name_list[0] = 'TOM'
print(name_list)

#逆置--reverse
num_list = [10,8,9,3,12,5]
num_list.reverse()
print(num_list)

#排序--sort（）
num_list.sort(reverse=True)  #默认reverse=False
print(num_list)

name_list.sort()
print(name_list)

num_list1 = sorted(num_list)
print(num_list1)

#复制--copy（）
new_list = num_list.copy()
print(new_list)

#列表循环遍历--while
#循环变量
i = 0
#循环条件
while i < len(num_list):
    #循环体
    print(num_list[i])
    #循环变量发生变化
    i += 1

#for
for i in num_list1:
    print(i)

#列表嵌套
name_list = [['Tom','Lily','Rose'],['小米','小红','小绿'],[10,20,30]]
print(name_list[2][1])

#应用
#导入随机数
import random
#定义列表
teacher_list = ['老师1','老师2','老师3','老师4','老师5','老师6','老师7','老师8']
room_list = [[],[],[]]
#遍历tacher列表
for teacher in teacher_list:
    i = random.randint(0,2)
    print(i)
    room_list[i].append(teacher)
print(room_list)