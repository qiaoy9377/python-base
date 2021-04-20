#求一个3*3矩阵中对角线上元素之和
'''
3 5 6
4 7 8
2 4 9
'''
matrix_list = [[3,5,6,1],[4,7,8,2],[2,4,9,3]]
def matrix_sum(matrix_list):
    #求主对角线数据之和，主对角线上的数据的位置等于行数
    #定义对角线之和变量
    result = 0
    #求列表长度
    length = len(matrix_list)
    #循环取列表下标
    for i in range(length):
        #找出主对角线数据进行累加
        result += matrix_list[i][i]
        #找出负对角线数据进行累加
        result += matrix_list[i][length-1-i]
    return result

print(matrix_sum(matrix_list))