def testA():
    a = 100
    print(a)

testA()
# print(a)   未定义不能打印

b = 200
def testB():
    global b
    b = 400
    print(b)

def testC():
    print(b)

testB()
testC()

c = 10
def testD():
    print(c)

def testE():
    global c
    c = 15
    print(c)

testD()
testE()

def fun1():
    return 50

def fun2(a):
    print(a)

fun2(fun1())

def fun3():
    return 1
    return 2    #多个return不执行

print(fun3())

def fun4(a):
    if a > 0:
        return '正数'
    else:
        return '非正数'

print(fun4(-1))

def fun5():
    return {1,2,2,2}

print(fun5())

#位置参数
def user_info(name,age,gender):
    print(f'我的名字是{name}，我的年龄是{age}，性别{gender}')

user_info('张三',18,'男')
user_info('xiaoming',gender='女',age=20)

def user_info1(name,age,id=100):
    print(f'我的名字是{name}，年龄{age}，学号{id}')

user_info1('wangli',21)
user_info1('李四',id=110,age=25)

def user_info2(*args):
    print(args)
user_info2('lily',18,'女','18800112134')

list1 = ['张三','man',21,10010]
user_info2(*list1)
t1 = ('tom',20,'nan')
user_info2(*t1)
set1 = {10,20,'zhangsan','男'}
user_info2(*set1)
user_info2()
user_info2(10)

def user_info3(**kwargs):
    print(kwargs)

user_info3(name = 'liyi',age = 20,学号=1100)
dict1 = {'name':'张三','age':21,'学号':1001}
user_info3(**dict1)

#拆包
#元组
def return_num(a,b):
    return a,b
num1,num2 = return_num(1,2)
print(num1,num2)

list1 = [10,20]
c,d = list1
print(c,d)

set2 = {100,'nan'}
e,f = set2
print(e,f)

#字典
key1,key2,key3 = dict1
print(key1,key2,key3)

a,b,c = dict1.values()
print(a,b,c)

#交换变量值
A = 1
B = 2
C = A
A = B
B = C
print(A,B)

A,B = B,A
print(A,B)

def look_id(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))
look_id(100)
look_id(12.5)
look_id(list1)
look_id(t1)
#look_id(set2)
look_id('Tom')
#look_id(dict1)

print(set2)
print(id(set2))
set2.add(10)
print(set2)
print(id(set2))

print(dict1)
print(id(dict1))
dict1['sex']='男'
print(dict1)
print(id(dict1))