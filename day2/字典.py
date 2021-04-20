#有数据字典
dict1 = {'name':'Tom','age':18,'gender':'男'}
#空字典
dict2 = {}
dict3 = dict()

#常见操作
#增--key不存在则新增
dict1['id'] = 110
print(dict1)
#改--key存在则修改
dict1['age'] = 20
print(dict1)

#删
# del dict1 #字典直接被删除
# print(dict1)  #报错，未定义

del dict1['id']
print(dict1)

#清空字典
dict1.clear()
print(dict1)

#查
#key值查找
dict1 = {'name':'Tom','age':19,'gender':'男'}
print(dict1['name'])
#print(dict1['id'])  #不存在报错

print(dict1.get('name','存在'))
print(dict1.get('id'))
print(dict1.get('id','不存在'))

#keys()
print(dict1.keys())
#values()
print(dict1.values())
#items()
print(dict1.items())

#遍历key
for key in dict1.keys():
    print(key)

#遍历value
for value in dict1.values():
    print(value)

#遍历元素
for item in dict1.items():
    print(item)

#遍历键值对
for key,value in dict1.items():
    print(f'{key}={value}')