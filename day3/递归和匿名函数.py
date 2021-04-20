
import functools

fn1 = lambda : 100
print(fn1())

fn2 = lambda a : print(2*a)
fn2(5)

fn3 = lambda b,c=2 : b+c
print(fn3(2,5))
print(fn3(2))

fn4 = lambda *args:args
print(fn4(10,20,30,'TOM'))
list1 = ['qwe',18,'男']
print(fn4(*list1))

fn5 = lambda **kwargs:kwargs
print(fn5(name='qwe',age = 20))
dict1 = {'name':'张三','age':21,'学号':1001}
print(fn5(**dict1))

fn6 = lambda a,b:a if a>b else b
print(fn6(1,2))

students = [
{'name':'张三','age':21,'学号':1101},
{'name':'lisi','age':20,'学号':1021},
{'name':'王五','age':11,'学号':10011}
]
# for i in range(len(students)):


students.sort(key=lambda x : x['name'])
print(students)

students.sort(key=lambda x : x['age'])
print(students)

students.sort(key=lambda x : x['学号'],reverse=True)
print(students)

fn7 = lambda X : X['name']
for i in students:
    print(fn7(i))

#高阶函数
def sum1(a,b):
    return abs(a)+abs(b)

print(sum1(-2,3))

def sum2(a,b,f):
    return f(a)+f(b)
print(sum2(-3,2,abs))

#map()
list1 = [10,20,30,15]
def fun1(x):
    return x**2

print(map(fun1,list1))
list2 = map(fun1,list1)
print(list(list2))

#reduce


def fun2(a,b):
    return a*b

result = functools.reduce(fun2,list1)

print(result)

#filter()
def fun3(a):
    return a>=20

data = filter(fun3,list1)
print(data)
list3 = list(data)
print(list3)

#递归
def sum_num(num):
    #判断如果为1，返回1，出口
    if num == 1:
        return 1
    #如果不是1，就执行这个
    return num + sum_num(num-1)

print(sum_num(3))