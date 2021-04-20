#一个元组可以存储多个数据，元组内的数据是不能修改的
#元组的特点：定义元组使用小括号，且逗号隔开各个数据，数据可以是不同的数据类型
#多数据元组
t1 = (10,20,30)
#但数据元组
t2 = (10,)  #如果定义的元组只有一个数据，那么这个数据后面也要添加逗号
print(type(t2))

t3 = (20)
print(type(t3))

t4 = ('hello')
print(type(t4))

#元组常见操作--元组数据不支持修改，只支持查找
#1、按下标查找
tuple1 = ('aa','bb','cc','bb')
print(tuple1[0])

#2.index()--查找某个数据，如果数据存在返回对应的下标，否则报错
print(tuple1.index('bb'))

#3.count()--统计某个数据在当前元组出现的次数
print(tuple1.count('bb'))

#4.len()--统计元组中数据的个数
print(len(tuple1))

#元组内的数据直接修改会报错
#tuple1[0] = 'aaa'

#如果元组里有列表，可以修改列表里的数据
tuple2 = (10,20,['aa','bb','cc'],50,30)
print(tuple2[2])  #访问到列表
tuple2[2][2] = 'ccc'
print(tuple2)