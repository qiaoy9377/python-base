#打印10000以内的完全平方数
#定义一个空列表用来存储数据
result_list = []
#循环遍历10000以内的数据
for num in range(10000):
    #将0-num之间的数作为除数，循环除，如果余数为0且商与除数相等则是完全平方数
    for div_num in range(1,num):
        #判断余数是否为0
        if num % div_num == 0:
            #判断商是否等于除数
            if num / div_num == div_num:
                result_list.append(num)

print(result_list)