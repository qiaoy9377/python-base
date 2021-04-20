#有一堆字符串“welcom to super&Test”，打印出tseT&repus ot 。。。。全部单词原位反转
#定义字符串
str1 = 'welcom to super&Test'
#将字符串转换为列表
list1 = list(str1)
print(list1)
#将列表数据逆置
list1.reverse()
print(list1)
#将列表数据拼接为字符串
print(''.join(list1))

#切片
str2 = str1[::-1]
print(str2)

#将列表从最后一个删除，然后将删除的数作为一个新列表
list2 = list(str1)
#print(list2)
str3 = ''
for i in range(len(list1)):
    del_name = list2.pop()
    str3 += del_name
print(str3)
