#break使用
string1 = 'hello world!'
for i in string1:
    if i == 'o' :
        print('o不打印')
        break
    print(i)

#continue使用
for i in string1:
    if i == 'o':
        print('遇到o，不打印')
        continue
    print(i)

#while..else
#else 循环可以和else配合使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码
i = 1
while i <= 5:
    print('我错了')
    i += 1
else:
    print('道歉正常完成')

#道歉5遍，第三遍不真诚，退出道歉循环，情况1：退出循环不道歉
i = 1
while i <= 5:
    print('我错了')
    if i == 3:
        print('道歉不真诚,更生气了，终止道歉')
        break
    i += 1
else:
    print('道歉完成')

#情况2：道歉不真诚继续道歉
i = 1
while i <= 5:
    if i == 3:
        print('道歉不真诚')
        i += 1
        continue
    print('我错了')
    i += 1
else:
    print('道歉完成')

#for else
string2 = 'hello world！'
for i in string2:
    print(i)
else:
    print('打印完成')

#break
string2 = 'hello world！'
for i in string2:
    if i == 'o':
        print('遇到o，不打印')
        break
    print(i)
else:
    print('执行完成')

#continue
string2 = "hello world!"
for i in string2:
    if i == 'o':
        print('遇到o，不打印')
        continue
    print(i)

else:
    print('执行完成')