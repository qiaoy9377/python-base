#打印变量的数据类型
a = 'hello world'
b = 'abcdefg'
print(type(a))
print(type(b))

#字符串输入
# name = input('请输入你的名字：')
# print(f'您输入的名字为{name}')
# print(type(name))
#
# password = input('请输入您的密码：')
# print('您输入的密码为%s'% password)
# print(type(password))

#字符串name=“abcdef”，取到不同下标对应的数据
name = 'abcdefg'
print(name[0])
print(name[1])
print(name[2])

#切片,负数代表倒数第几个数
print(name[2:5:1])
print(name[2:5])
print(name[:5])
print(name[1:])
print(name[:])
print(name[::2])
print(name[:-1]) #表示倒数第一个数
print(name[-4:-1])
print(name[::-1])

#查找字符串内容
mystr = "hello world and superctest and chaoge and Python"
print(mystr.find('and'))
print(mystr.find('and',15,30))
print(mystr.find('ands'))

print(mystr.index('and'))
print(mystr.index('and',15,30))
#print(mystr.index('ands'))--报错

print(mystr.rfind('and'))
print(mystr.rfind('and',15,30))
print(mystr.rfind('ands'))

print(mystr.rindex('and'))
print(mystr.rindex('and',15,30))
#print(mystr.rindex('ands'))--报错

print(mystr.count('and'))
print(mystr.count('and',0,15))
print(mystr.count('ands'))

#修改-replace
print(mystr.replace('and','he'))
print(mystr.replace('and','he',1))
print(mystr.replace('and','he',5))

#split
print(mystr.split('and'))
print(mystr.split('and',2))
print(mystr.split('and',5))
print(mystr.split(' '))

#join()
print('_'.join(mystr))
list1 = ['hello','world','!']
print('-'.join(list1))
t1 = ('a','b','c','d','1','2')
print('...'.join(t1))

#capitalize()
print(mystr.capitalize())

#title()
print(mystr.title())

#lower()
mystr1 = mystr.title()
print(mystr1)
print(mystr1.lower())

#upper()
print(mystr.upper())

#删除字符串的空白字符lstrip（）、rstrip（）、strip（）
mystr2 = '     hello world he superctest he chaoge he Python    '
print(mystr2.rstrip())
print(mystr2.lstrip())
print(mystr2.strip())

#ljust()
mystr3='hello'
print(mystr3.ljust(10))
print(mystr3.ljust(8,'~'))

#rjust()
print(mystr3.rjust(10,'.'))
print(mystr3.rjust(8))

#center()
print(mystr3.center(10))
print(mystr3.center(8,'-'))

#判断-startswith()
print(mystr.startswith('hello'))
print(mystr.startswith('h',5,10))

#endswith()
print(mystr.endswith('thon'))
print(mystr.endswith('thon',-10,-1))

#isalpha()
mystr4 = 'abcd123'
print(mystr3.isalpha())
print(mystr4.isalpha())

#isdigit()
mystr5 = '12345'
print(mystr4.isdigit())
print(mystr5.isdigit())

#isalnum()
print(mystr.isalnum())
print(mystr4.isalnum())

#isspace()
mystr6 = '   '
print(mystr.isspace())
print(mystr6.isspace())