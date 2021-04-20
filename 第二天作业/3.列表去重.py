#列表去重
#1.通过数据类型转换去重
list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
set1 = set(list1)
print(set1)
list2 = list(set1)   #通过容器类型转换会打乱列表的顺序
print(list2)

#2、通过判断去重--for循环
list3 = []
for i in list1:
    if i not in list3:
        list3.append(i)
    else:
        pass
print(list3)

#3、通过判断去重-while循环
list4 = []
#循环变量--列表参数下标
i = 0
#循环判断，判断下标是否在列表内
while i < len(list1):
    #循环体
    if list1[i] not in list4:
        list4.append(list1[i])
    #循环变量发生变化
    i += 1
print(list4)