#while循环
#循环变量-行数
i = 5
#循环条件
while 0 < i <= 5:
    #循环体
    #循环变量
    str1 = ''
    n = 0
    #循环条件
    while n < i:
        #循环体
        str1 += '* '
        #循环变量发生变化
        n += 1
    #循环变量发生变化
    i -= 1
    print(str1.center(10))
#for循环
for i in range(5,0,-1):
    str2 = ''
    for n in range(i):
        str2 += '* '
    print(str2.center(10))