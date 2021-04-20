#有一堆字符串，‘abcdef’，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
#定义字符串
str1 = 'abcdef'
#创建一个空列表
list1 = []
#逆着循环取出字符串的数据，插入列表
#1、使用while循环
l = len(str1)
#循环变量--数据下标
i = l-1
#循环判断-判断下标大于等于0
while i >= 0:
    #循环体--取数据插入列表
    list1.append(str1[i])
    #循环变量发生变化
    i -= 1
print(''.join(list1))

#2、使用for循环实现
list2 = []
for i in str1[::-1]:
    list2.append(i)
print(''.join(list2))