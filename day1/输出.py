age = 18
id = 4
name = 'Tom'
print('今年我的年龄是%d'%age)
print('我的id是%06d'%id)   #不写0的话就是补空格
print('我的年龄是%d，id是%04d，明年我就%d岁了'%(age,id,age+1))
print(f'我的姓名是{name}，明年我就{age+1}岁了')

num = 10/5
print(num)
print('%.2f'%num)

print('123\t456')
print('123\n456')


#练习
password=input('请输入您的密码：')  #输入
print('您输入的密码为：%s' % password)  #格式化输出-%形式
print(f'您输入的密码为：{password}')   #格式化输出-f表达式的形式
print(type(password))