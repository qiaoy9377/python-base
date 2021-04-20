#定义字符串
str1 = 'welocme to super&Test'
#将字符串进行分割
list1 = str1.split(' ')
#print(list1)
#建立一个空列表，用来存储反转后的字符串
list2 = []
#循环遍历每个字符串
for i in list1:
    #将每个字符串进行反转
    j = i[::-1]
    #print(j)
    #将反转后的字符串加入新列表
    list2.append(j)
#将反转之后的列表元素拼接成字符串
str2 = ' '.join(list2)
print(str2)

