#有数据集合
s1 = {10,20,30,40,50}
print(s1)

s2 = {10,30,20,10,30,40,30,50}
print(s2)

s3 = set('abcdefg')
print(s3)

#空集合
s4 = set()
print(type(s4))

s5 = {}
print(type(s5))

#常见操作方法
#增--add()--追加单个数据
s1.add(10)   #追加已有数据，不进行任何操作
print(s1)

s1.add(60)
print(s1)

#update()--追加的是序列
s1.update((100,200))
print(s1)

s1.update([1000,2000])
print(s1)

s1.update({10000,20000})
print(s1)

s1.update('abc')
print(s1)

# s1.update(1)   #报错，追加序列，不能追加单个
# print(s1)

#删除
#remove（）
s1.remove(1000)
print(s1)

# s1.remove('d')  #不存在，则报错
# print(s1)

#discard（）
s1.discard(10000)
print(s1)

s1.discard('d')  #不存在，不报错
print(s1)

#pop（）--随机删除，并返回该数据
del_num = s1.pop()
print(del_num)
print(s1)

#查找数据
print('a' in s1)
print('d' not in s1)
print(2000 not in s1)