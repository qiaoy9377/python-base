#实现函数get_max,函数最终返回列表lst的最大值，不要使用max函数
lst = [4,2,1,6,7,9]
#定义求列表最大值的函数
def get_max(lst):
    '''
    返回列表lst的最大值
    :param lst: 列表
    :return: 最大值
    '''
    #将列表第一个值赋值给最大值变量
    max_num = lst[0]
    #循环遍历列表数据
    for i in lst:
        if i > max_num:
            max_num = i
    return max_num

max_value = get_max(lst)
print(max_value)
