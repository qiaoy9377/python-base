
def fib(num):
    '''
    求斐波那契数列
    :param num: 斐波那契数列的第几个数
    :return:
    '''
    #如果是前两个数则返回1
    if num == 1 or num == 2:
        return 1
    #返回前两个数之和
    return fib(num-1)+fib(num-2)

print(fib(8))