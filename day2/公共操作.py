#+
#1.字符串
str1 = 'aa'
str2 = 'bb'
str3 = str1 + str2
print(str3)

#2.列表
list1 = [1,2]
list2 = [10,20]
list3 = list1+list2
print(list3)

#3.元组
t1 = (1,2)
t2 = (10,20)
t3 = t1+t2
print(t3)

#*
#1.字符串
str4 = str1*3
print(str4)
print('-'*10)

#2.列表
list4 = list1 *4
print(list4)

#3.元组
t4 = t1 * 3
print(t4)

#in\not in
#1.字符串
print('a' in 'and')
print('a' not in 'hello')
#2.列表
print(1 in list1)
print(2 not in list1)
#3.元组
print(1 in t1)
print(3 not in t1)
#4.字典
dict1 = {'name':'Tom','age':18,'id':110}
print('id' in dict1)
print('Tom' not in dict1.values())
print(('age',19)  not in dict1.items())

#len()
#1.字符串
print(len(str3))

#2.列表
print(len(list3))

#3.元组
print(len(t3))

#4.集合
set1 = {10,20,3,5}
print(len(set1))

#5.字典
print(len(dict1))

#del（）
#1.字符串
str1 = 'abcdefg'
#del  str1
#print(str1)  #被删除了，报错，未定义

#2.列表
del(list3[2])
print(list3)

del list3[1]
print(list3)

#max()
#1.字符串
print(max(str1))
#2.列表
print(max(list3))
#元组
print(max(t3))
#字典
print(max(dict1))
#集合
print(max(set1))

#min（）
print(min(str1))
print(min(list3))
print(min(t3))
print(min(dict1))
print(min(set1))

#range()
for i in range(1,10,2):
    print(i)

for i in range(5):
    print(i)

for i in range(5,1,-1):
    print(i)

#enumarate()
list1 = ['a','b','c','d','e']
for i in enumerate(list1):
    print(i)

for i in enumerate(list1,start=1):
    print(i)

for index,value in enumerate(list1,start=2):
    print(f'下标为{index}，值为{value}')