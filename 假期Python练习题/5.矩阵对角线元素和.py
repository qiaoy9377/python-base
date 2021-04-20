#求一个3*3矩阵中对角线上元素之和
'''
3 5 6
4 7 8
2 4 9
'''
def juzheng_sum(juzheng_list):
    '''
    求矩阵正负对角线之和的函数
    :param juzheng_list: 矩阵按照顺序以列表形式输入
    :return: 正负对角线之和
    '''
    #输入矩阵的阶数
    juzheng_num = int(input('请输入矩阵的阶数：'))
    #循环取矩阵列表中符合要求的下标的数据--主对角线
    #循环变量-矩阵数据下标
    i = 0
    result = 0
    list_i = []
    #循环判断
    while i < len(juzheng_list):
        #循环体-求主对角线之和
        list_i.append(i)
        result += juzheng_list[i]
        #循环变量发生变化-主对角线每个数据下标增加矩阵阶数+1
        i += juzheng_num+1

    #循环变量--矩阵负对角线下标
    j = juzheng_num-1
    #循环判断-判断下标小于列表长度
    while j < len(juzheng_list):
        #循环体-求负对角线之和
        #判断j是否存在i下标的列表中，存在代表取值重复，不做累加
        if j not in list_i:
            result += juzheng_list[j]
        #循环变量发生变化
        j += juzheng_num-1

    return result

#将矩阵数据存入列表
list1 = [3,5,6,4,7,8,2,4,9]
print(juzheng_sum(list1))