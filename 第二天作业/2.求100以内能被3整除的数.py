#while循环
#循环变量-数据
num = 0
list1 = []
#循环判断-判断数据是否在100以内
while num <= 100:
    #循环体
    if num % 3 == 0:
        list1.append(num)
    #循环变量发生变化
    num += 1
print(list1)

#for循环
list2 = []
for num in range(101):
    if num % 3 == 0:
        list2.append(num)
print(list2)

#推导式
list3 = [num for num in range(101) if num % 3 == 0]
print(list3)