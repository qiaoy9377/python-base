#元组存储所有的数据类型，但是不可修改
#多个数据元组
t1 = (10,20,30)

#单个数据元组
t2 = (10,)
print(type(t2))

t3 = (20)
print(type(t3))

t4 = ('hello')
print(type(t4))

#常见操作--查找
#按下标查找
tuple1 = ('aa','bb','cc','bb')
print(tuple1[1])

#index()
print(tuple1.index('cc'))
#print(tuple1.index('dd'))  #找不到报错

#count（）
print(tuple1.count('bb'))

#len()
print(len(tuple1))

#元组中有列表，可以修改列表中的数据
tuple2 = (10,20,['aa','bb','cc'],50,30)
tuple2[2][1] = 'bbb'
print(tuple2)

print(tuple2.index(['aa','bbb','cc']))

#容器转换
#tuple（）
list1 = [10,20,30,40,20,50,15]
s1 = {100,200,15,20,150,50,20}
print(tuple(list1))
print(tuple(s1))

#list()
t1 = ('a','b','c','d','a','e')
print(list(t1))
print(list(s1))

#set()--去重，不支持下标，大括号括起来的都不支持下标
print(set(list1))
print(set(t1))