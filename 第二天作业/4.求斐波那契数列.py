#斐波那契数列是前两个数之和等于第三个数
#方法一：
#定义前两个数
num1 = num2 = 1
#创建一个空列表
list1 = []
#将数据插入列表
list1.extend([num1,num2])
#print(list1)
#循环变量--列表数据下标
i = 0
#循环判断--假定判断数列长度为10
while i < 10:
    #循环体
    num = list1[i]+list1[i+1]
    list1.append(num)
    #循环变量发生变化
    i += 1
print(list1)

#方法二
list2 = [1,1]
for i in range(10):
    num = list2[i] + list2[i+1]
    list2.append(num)
print(list2)

#方法三
a = b = 1
list3 = []
for i in range(10):
    list3.append(a)
    c = a + b
    a = b
    b = c
print(list3)