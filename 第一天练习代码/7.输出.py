age = 18
name = 'Tom'
weight = 75.5
student_id = 1

#我的名字是TOM
print('我的名字是%s'% name)

#我的学号是0001
print('我的学号是%04d'% student_id)

#我的体重是75.50公斤
print('我的体重是%.2f'% weight)

#我的名字是Tom，今年18岁了
print('我的名字是%s，今年%d岁了'% (name,age))

#我的名字是Tom，明年19岁了
print('我的名字是%s，明年%d岁了' % (name,age+1))

print(f'我的名字是{name}，明年{age+1}岁了')