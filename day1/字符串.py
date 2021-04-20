# print("I'm Tom")
#
# #下标  下标是从0开始的
# name = 'abcdefg'
# print(name[0])
# print(name[3])
#
# #切片
# print(name[2:5:1])
# print(name[2:5])
# print(name[:4])
# print(name[1:])
# print(name[:])
# print(name[:2])
# print(name[:-1])
# print(name[-3:-2])
# print(name[::-1])
# print(name[6:3:-1])
# print(name[2:5:-1])  #没切到，为空值
# print(name[-1::-2])

#常用操作方法
#1、查找--find（）、index（）、rfind（）、rindex（）、count（）
mystr = "hello world and Superctest and chaoge and Python"

print(mystr.find('and'))
print(mystr.find('and',16,30))
print(mystr.find('ands'))
print(mystr.index('and'))
print(mystr.index('and',30))
#print(mystr.index('ands'))
print(mystr.rfind('and'))
print(mystr.rfind('and',15,30))
print(mystr.rindex('and'))
print(mystr.rindex('and',0,15))
print(mystr.count('and'))
print(mystr.count('and',0,30))

#2、修改-replace（）、split（）、join（）、capitalize（）、title（）、lower（）、upper（）、lstrip（）、rstrip（）、strip（）
#ljust（）、rjust（）、center（）
print(mystr.replace('and','he'))
print(mystr.replace('and','he',2))
print(mystr.replace('and','he',5))
print(mystr.split('and'))
print(mystr.split(' ',3))
print(mystr.split('and',5))

print('-'.join(mystr))
list1 = ['hello','python']
print('...'.join(list1))

print(mystr.capitalize())
print(mystr.title())
print(mystr.lower())
print(mystr.upper())

mystr1 = '  hello python   '
print(mystr1.lstrip())
print(mystr1.rstrip())
print(mystr1.strip())

print(mystr1.ljust(30,'.'))
print(mystr1.rjust(25,'-'))
print(mystr1.center(28,'-'))

#3、判断--startswith()、endswith()、isalpha（）、isdigit（）、isalnum（）、isspace（）
mystr2 = '123456'
mystr3 = 'hello'
mystr4 = 'hello12345'
mystr5 = '   '
print(mystr1.startswith('  hello'))
print(mystr1.endswith('python'))
print(mystr1.isalpha())
print(mystr3.isalpha())
print(mystr1.isdigit())
print(mystr2.isdigit())
print(mystr1.isalnum())
print(mystr4.isalnum())
print(mystr1.isspace())
print((mystr5.isspace()))