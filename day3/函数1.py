#需求：复现ATM机取钱功能

#先定义后使用，把函数挪到前面
def select_func():
    print('------请选择功能-------')
    print('查询')
    print('取钱')
    print('退卡')
    print('存钱')
    print('--------------')

print('密码正确登录成功')
#显示选择功能界面--调用函数
select_func()
print('查询余额完毕')
#显示选择功能界面
select_func()
print('取了2000元钱')
#显示选择功能界面
select_func()

#函数的参数
def add(a,b):
    sum1 =  a + b
    print(sum1)

add(3,4)


#函数的返回值
def add(a,b):
    return a + b

sum2 = add(2,3)
print('两个数之和为：%s'% sum2)

def buy():
    '''

    :return:
    '''
    print('我家有烟')
    return '烟'

goods = buy()
print('我买到的商品为：', goods)

def printline(a):
    '''
    返回一条线
    :param a: '-'的个数
    :return:
    '''
    #return '-'*a
    print('-'*a)

def printlines(b):
    '''
    打印多条线
    :param b: 线的数量
    :return: 线的内容
    '''
    # oneline = printline(5)
    # print(oneline*b)       打印出的线没有换行
    for i in range(b):
        # oneline = printline(5)
        # print(oneline)
        printline(7)

printlines(6)
help(printlines)
help(printline)

#求3个数之和
def sum1(a,b,c):
    return a+b+c

def avg(a,b,c):
    sum2 = sum1(a,b,c)
    # anverange = sum2/3
    # print(anverange)
    return sum2/3


print(avg(2,4,5))
