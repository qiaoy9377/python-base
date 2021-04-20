#有一堆字符串，‘aabbbcddef’，输出abcdef
#定义字符串
str1 = 'aabbbcddef'
#定义一个空列表
list1 = []
#循环取字符串的数据插入列表，如果已存在就不再插入
#1、使用while循环
#循环变量--字符串下标
i = 0
#循环判断-下标小于字符串长度
while i < len(str1):
    #循环体-判断是否存在列表中，不存在即添加到列表
    if str1[i] not in list1:
        list1.append(str1[i])
    #循环变量发生变化
    i += 1
#打印字符串
print(''.join(list1))

#2、for循环实现
#定义一个空列表
list2 = []
#循环取字符串的数据
for i in str1:
    #判断列表中是否存在,不存在即添加到列表中
    if i not in list2:
        list2.append(i)
#打印字符串
print(''.join(list2))

#方法三
str2 = ''
for i in str1:
    if i in str2:
        pass
    else:
        str2+=i
print(str2)