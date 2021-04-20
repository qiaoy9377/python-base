#输出所有的水仙花数
#定义一个空列表，用来存水仙花数
result_list = []
#循环取所有的三位数
for num in range(100,1000):
    #将数据类型转换为字符串
    num_str = str(num)
    #循环遍历字符串，将每个数据都进行3次方计算并相加
    result = 0  #初始结果为0
    for i in num_str:
        one_result = int(i)**3   #1个数的3次方
        result += one_result     #将每个数的3次方进行累加
    #判断如果累加和等于该数，则添加到列表
    if num == result:
        result_list.append(num)

print(result_list)

