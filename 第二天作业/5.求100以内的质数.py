#质数只能被1和它本身整除
#1、while循环
#定义一个空列表
list1 = []
#循环变量--数据2是最小的质数，从2开始
num = 2
#循环判断--判断数据是否小于100
while num <= 100:
    #循环体
    #循环变量--除数
    i = 2
    #循环判断--判断除数小于数据
    while i < num:
        #循环体
        #判断是否能够整除，如果出现能够整除的就终止循环
        if num % i == 0:
            break
        #循环变量发生变化
        i += 1
    # 如果不能整除，循环执行完毕则该数为质数，加入列表当中
    else:
        list1.append(num)
    #循环变量发生变化
    num += 1
print(list1)

#2、for循环
#定义一个空列表
list2 = []
#循环访问100以内的数
for i in range(2,100):
    #循环访问i以内的数作为除数
    for j in range(2,i):
        #判断是否能够整除，如果出现能够整除的就终止循环
        if i % j == 0:
            break
    #如果不能整除，循环执行完毕则该数为质数，加入列表当中
    else:
        list2.append(i)
print(list2)