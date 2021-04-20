def fib_num(num):
    '''
    斐波那契数列
    :param num: 斐波那契数列的数量
    :return: 数列列表
    '''
    #出口，如果两个数返回[1,1]
    if num == 2:
        return [1,1]
    #将每次返回的斐波那契数列列表实例化
    fib_list = fib_num(num-1)
    #求出返回的数列长度
    l = len(fib_list)
    #下一个列表新增的数等于前一个列表最后两个数之和
    result = fib_list[l-2]+fib_list[l-1]
    #返回斐波那契数列，是前一次的列表加最新增的数
    return fib_num(num-1)+[result]
print(fib_num(10))
