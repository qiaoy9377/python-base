#定义列表
list1 = ['1','2','3']
list2 = []
#循环遍历列表数据
for i in list1:
    #将数据转换为原始的数据类型
    j = eval(i)
    #print(j)
    #将转换后的数据存入新的列表
    list2.append(j)
print(list2)