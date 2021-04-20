#使用列表推导式生成100以内能被5整除的数
list1 = [i for i in range(101) if i % 5 == 0]
print(list1)