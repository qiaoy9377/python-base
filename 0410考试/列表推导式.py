#用列表推导式得出1-100能被3整除的数
list1 = [i for i in range(1,101) if i % 3 == 0]
print(list1)