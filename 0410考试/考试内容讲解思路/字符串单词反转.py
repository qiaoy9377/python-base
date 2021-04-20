str1 = 'welocme to super&Test'
#将字符串用空格切割
list1 = str1.split(' ')
#定义一个空列表，用来存储转换后的字符串
list3 = []
#循环遍历列表元素
for str2 in list1:
    #将字符串转换为列表
    list2 = list(str2)
    #获取字符串的长度
    l = len(str2)
    for i in range(l//2):
        #将字符串的位置进行互换
        list2[i],list2[l-1-i] = list2[l-1-i],list2[i]
    #将列表内容拼接为字符串
    str3 = ''.join(list2)
    #将字符串插入列表
    list3.append(str3)

str4 = ' '.join(list3)
print(str4)

