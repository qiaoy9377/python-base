#一、打印三角形
#1.while实现
#循环变量--行号
j = 1
#循环判断--判断行号小于5
while j <= 5:
    #循环体--循环打印单行星号
    #循环变量-星号数量
    i = 0
    str1 = ''  #定义一个字符串
    #循环判断--判断星号数量
    while i < j:
        #循环体--用星号拼接字符串
        str1 += '*'
        #循环变量发生变化
        i += 1
    #打印拼接好的星号字符串
    print(str1)
    #循环变量发生变化
    j += 1

#用for实现
#行数循环
for j in range(1,6):
    str2 = ''   #定义一个空的字符串
    #每行打印星号循环
    for i in range(j):
        str2 += '*'
    print(str2)

#二、打印靠右对齐的三角形
#1.while循环
j = 1
while j <= 5:
    str1 = ''
    i = 0
    while i < j :
        str1 += '*'
        i += 1
    print(str1.rjust(5))  #调整打印出的字符串为右对齐格式
    j += 1

#for循环
for j in range(1,6):
    str2 = ''
    for i in range(j):
        str2 += '*'
    print(str2.rjust(5))  #调整打印出的字符串为右对齐格式

#三、上下颠倒的三角形
#1.while循环
#循环变量
j = 5  #上下颠倒，第一行变成5个了，所以行数起始值调整为最大值
#循环条件
while j > 0:
    #循环体
    #循环变量
    i = 0
    str1 = ''
    #循环判断
    while i < j:
        #循环体
        str1 += '*'
        #循环变量变化
        i += 1
    print(str1)
    #循环变量
    j -= 1

#2.for循环
for j in range(5,0,-1):
    str2 = ''
    for i in range(j):
        str2 += '*'
    print(str2)

#四、靠右对齐上下颠倒
#while循环
j = 5
while j > 0:
    i = 0
    str1 = ''
    while i < j:
        str1 += '*'
        i += 1
    print(str1.rjust(5))
    j -= 1
#for循环
for j in range(5,0,-1):
    str2 = ''
    for i in range(j):
        str2 += '*'
    print(str2.rjust(5))

#五、正三角形
#1.while循环
j = 1
while j <= 5:
    i = 0
    str1 = ''
    while i < j:
        str1 += '* '
        i += 1
    print(str1.center(9))
    j += 1

#2.for循环
for j in range(1,6):
    str2 = ''
    for i in range(j):
        str2 += '* '
    print(str2.center(10))

#六、菱形
#1.正三角形和倒三角形拼接
for j in range(1,6):
    str3 = ''
    for i in range(j):
        str3 += '* '
    print(str3.center(10))
for j in range(4,0,-1):
    str4 = ''
    for i in range(j):
        str4 += '* '
    print(str4.center(10))

#2.结合if。。。else。。。打印菱形
for j in range(5):
    str5 = ''
    if j <= 2:
        for i in range(j+1):
            str5 += '* '
        print(str5.center(10))
    else:
        for i in range(5,j,-1):
            str5 += '* '
        print(str5.center(10))