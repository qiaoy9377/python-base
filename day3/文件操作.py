# #打开文件
# f = open('test.txt','a',encoding='UTF-8')
# #写入文件
# f.write('hello world')
# f.write('hi world')
# #关闭文件
# f.closed
#
# f1 = open('test.txt','w+')
# print(f1.read())
# f1.write('12345')
# print(f1.read())

# f = open('test.txt')
# print(f.read(5))
# print(f.readlines())
# f.seek(0,0)
# print(f.read())
# f.seek(0,0)
# print(f.readline())
# print(f.readline())
# f.seek(5,0)
# print(f.readline())
# print(f.read())

# f = open('test.txt','r+')
# #f.seek(0,2)
# f.write('ABCDe')
#
# print(f.read(10))
#
# f.write('12345')
# f.seek(0,0)
# print(f.read())

import os

# os.rename('test1.txt','test1-rename.txt')
# os.remove('test1-rename.txt')
#os.mkdir('test')
#os.rmdir('test')
print(os.getcwd())
os.chdir('..')  #跳到当前目录的上一级
print(os.getcwd())
print(os.listdir())
os.chdir('.\\day2')
print(os.getcwd())
print(os.listdir())

os.chdir('..\\day3')
print(os.getcwd())
f = open('ceshi.txt','w')