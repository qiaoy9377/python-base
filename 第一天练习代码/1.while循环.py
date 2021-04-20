#循环输出
i = 0
while i < 5:
    print('你好')
    i+=1
print('循环完成')

#1-100累加
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1

print(sum)

#1-100的偶数累加方法一
i = 0
sum = 0
while i <=100:
    sum += i
    i += 2

print(sum)

#1-100的偶数累加方法二
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print(sum)

#break和continue

#break：吃苹果吃饱了就终止吃苹果--终止此循环
i = 1
while i <= 5:
    if i == 4:
        print('吃饱了')
        break
    print(f'吃了第{i}个苹果了')
    i += 1
#print('苹果都吃完啦')

#continue：吃苹果吃出了虫子换个苹果继续吃--退出当前一次循环继而执行下一次循环代码
i = 1
while i <= 5:
    if i == 3:
        print(f'吃到虫子啦,第{i}个苹果不吃了')
        i += 1
        continue
    print(f'吃第{i}个苹果')
    i += 1

#while循环内嵌
#道歉惩罚措施连续执行3天
j = 1
while j <= 3:
    i = 1
    while i <= 3:
        print('我错了')
        i += 1
    print("外加拖地、洗碗")
    print(f"-------第{j}天任务完成--------")
    j += 1
print("惩罚结束")

#循环嵌套应用一：打印星号（正方形）
j = 1
while j <= 5:
    i = 1
    while i <= 5:
        print('* ',end='') #按行打印不能换行，用来取消print默认结束符\n
        i += 1
    print() #每行结束后需要换行，借助空print()，作为默认结束符换行
    j += 1
print('打印完成')

#循环嵌套应用二：打印星号（三角形）
j = 1
while j <= 5:
    i = 1
    while i <= j:
        print('*', end='')
        i += 1
    print()
    j += 1
print('打印完成')

#九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={i*j}',end=' ')
        i += 1
    print()
    j += 1
