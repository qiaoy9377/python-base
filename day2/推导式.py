#创建一个0-10的列表
#用while实现
#循环变量
num = 0
list1 = []
#循环条件
while num <= 10:
    #循环体
    list1.append(num)
    #循环变量发生变化
    num += 1
print(list1)

#用for实现
list2 = []
for num in range(11):
    list2.append(num)
print(list2)

list3 = [i for i in range(11)]
print(list3)

#需求：创建0-10的偶数列表
#用while实现
#循环变量
num = 0
list1 = []
#循环条件
while num <= 10:
    #循环体
    if num % 2 == 0:
        list1.append(num)
    #循环变量发生变化
    num += 1
print(list1)

#用for实现
list2 = []
for i in range(11):
    if i % 2 == 0:
        list2.append(i)
print(list2)

#推导式
list3 = [i for i in range(11) if i % 2 == 0]
print(list3)

list4 = [i for i in range(0,11,2)]
print(list4)

#for循环嵌套
list1 = []
for i in range(1,3):
    for j in range(3):
        list1.append((i,j))
print(list1)

#推导式
list1 = [(i,j) for i in range(1,3) for j in range(3)]
print(list1)

#两个列表合并为一个字典
list1 = ['name','age','gender']
list2 = ['Tom',20,'男']
#用for实现
dict1 = {}
for i in range(len(list2)):
    dict1[list1[i]] = list2[i]
print(dict1)

#用while实现
dict2 = dict()
#循环变量
i = 0
#循环条件
while i < len(list1):
    #循环体
    dict2[list1[i]] = list2[i]
    #循环变量发生变化
    i += 1
print(dict2)

dict3 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict3)

#创建一个字典，字典key是1-5数字，value是这个数字的2次方
dict4 = {i:i**2 for i in range(1,6)}
print(dict4)

#提取字典中目标数据
count1 = {'MBP':268,'HP':125,'DELL':201,'Lenovo':199,'acer':99}
count2 = {key:value for key,value in count1.items() if value >= 200}
print(count2)

#集合推导式
#创建一个集合，数据为下方列表的2次方
list1 = [1,2,1,4,3]
set1 = {i**2 for i in list1 }
print(set1)  #去重