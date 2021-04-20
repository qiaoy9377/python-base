#有一堆字符串“aabbcddef”打印出不重复的字符串结果：cef
#定义字符串
str1 = 'aabbcddef'
#1、while循环
#字符串是不可变类型，故先创建一个空列表，将字符串中取到的数据添加到列表中
list1 = []
#循环取字符串中的数据，计算该子串的个数，大于1则不要，否则存入列表
#循环变量-字符串下标
i = 0
#循环判断--判断下标小于字符串长度
while i < len(str1):
    #循环体-根据下标取子串，判断子串出现次数
    j = str1.count(str1[i])
    if j == 1:
        list1.append(str1[i])
    #循环变量发生变化
    i += 1
#打印字符串
print(''.join(list1))

#2、for循环
#定义1个空列表
list2 = []
#循环取出字符串中的数据
for i in str1:
    #判断该子串出现的次数，如果等于1则插入列表
    if str1.count(i) == 1:
        list2.append(i)
#打印字符串，将列表字符串元素拼接成字符串
print(''.join(list1))

str2 = ''
for i in str1:
    if str1.count(i) == 1:
        str2 += i
print(str2)

