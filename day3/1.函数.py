#局部变量
def testA():
    a = 100
    print(a)

testA()

#print(a)  #报错，提示a未定义

#全局变量
a = 100

def testA():
    print(a)

def testB():
    print(a)

testA()
testB()

#在函数内部修改变量
def testB():
    a = 200
    print(a)
testB()
print(f'全局变量a的值为{a}')

#在函数内部修改全局变量的值
b = 10
def testAA():
    print(b)

def testBB():
    global b  #global关键字声明b为全局变量
    b = 20
    print(b)

testAA()
testBB()
print(f'全局变量b的值为{b}')

#共用全局变量
global_num = 0
def A ():
    global global_num
    global_num = 10

def B():
    print(global_num)

A()
B()

#返回值作为参数
def C():
    return 50

def D(num):
    print(num)

result = C()
D(result)

#函数的返回值
def fun1():
    return 1
    return 2

def fun2():
    return 1,2

num1 = fun1()
num2 = fun2()
print(num1)
print(num2)

def user_info(name,age,gender='man'):
    print(f'您的姓名是{name}，年龄是{age}，性别是{gender}')

user_info('Tom',18,'男')

user_info(name='Rose',gender='女',age=20)
user_info('Lily',gender='woman',age=20)

user_info('xiaoming',18)

def user_information(*args):
    print(args)

user_information('TOM',20,'MAN')
list1 = [1,2,3]
user_information(*list1)

def user(**kwargs):
    print(kwargs)

user(name='Tom',age=19,gender='男')
dict1 = {'name':'Tom','age':18,'gender':'男'}
user(**dict1)

#拆包
#元组
def return_num():
    return 10,20

num1,num2 = return_num()
print(num1)
print(num2)

dict1 = {'name':'Tom','age':18}
a,b=dict1
print(a)
print(b)

print(dict1[a])
print(dict1[b])

#交换变量值
#方法一
a = 1
b = 2
c = 0
c = a
a = b
b = c
print(a)
print(b)

#方法二
a,b = b,a
print(a)
print(b)

#用id来判断两个变量是否为同一个值引用
#1.int类型
a = 1
b = a
print(b)
print(id(a))
print(id(b))

a = 2
print(b)  #不可变类型
print(id(a))
print(id(b))

#2.列表
aa = [1,2,3]
bb = aa
print(bb)
print(id(aa))
print(id(bb))

aa.append(4)
print(bb)  #列表为可变类型
print(id(aa))
print(id(bb))

#引用当参数
def test1(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))

test1(10)

c = [10,20]
test1(c)