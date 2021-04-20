#1.float（）-将数据转换成浮点型
num1 = 1
print(num1)
print(float(num1))
print(type(float(num1)))

#2.str()-将数据转换为字符串类型
num2 = 10
print(str(num2))
print(type(str(num2)))

#3.tuple()-将一个序列转换成元组
list1 = [1,2,3,4,5,2,5]
print(tuple(list1))
print(type(tuple(list1)))

#4.list()-将一个元组转换成列表
tuple1 = (1,2,3,4,5)
print(list(tuple1))
print(type(list(tuple1)))

#5.eval()-将字符串中的数据转换成python表达式原本类型
str1 = '10'
str2 = '[1,2,3,4,5]'
str3 = '(1,2,3,4,5)'
str4 = '{1,2,3,4,5}'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))