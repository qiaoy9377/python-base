#有一堆字符串“welcom to super&Test”，打印出superTest，不能查字符串的索引
#定义字符串
str1 = 'welcom to super&Test'
#将字符串用空格切片
list1 = str1.split(' ')
print(list1)
#将列表第3个参数赋值给字符串2
str2 = list1[2]
print(str2)
#将str2进行切片
list2 = str2.split('&')
print(''.join(list2))

#再次切片，判断切片完成后的长度
for i in list1:
    list3 = i.split('&')
    if len(list3) > 1:
        str3 = ''.join(list3)
print(str3)