#实例1
num = input('请输入您的幸运数字：')
print('您输入的幸运数字是%s'%num)
print(type(num))
print(type(int(num)))

#实例2
#转换为浮点型
num = 1
print(float(num))
print(type(float(num)))
#转换为字符串类型
num2 = 10
print(type(str(num2)))
#将一个序列转换成元组
list1 = [10,20,30]
print(type(list1))
print(tuple(list1))
print(type(tuple(list1)))

#将一个序列转换为列表
t1 = (100,200,300)
print(type(t1))
print(list(t1))
print(type(list(t1)))

#将字符串中的数据转换成python表达式原本类型
str1 = '10'
str2 = '[1,2,3]'
str3 = '(1000,2000,3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))

