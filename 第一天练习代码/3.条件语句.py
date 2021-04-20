#练习1
if True:
    print('条件语句1')
    print('条件语句2')

print('无论条件是否成立都打印')

#如果用户年龄大于等于18岁，即成年，输出’已成年，可上网‘
age = 18
if age >= 18:
    print('已经成年，可以上网')

age = int(input('请输入年龄：'))  #input接受用户输入的数据是字符串类型，这里需要int转换数据类型
if age >= 18:
    print(f'你的年龄是{age}，已经成年，可以上网')
else:
    print(f'你的年龄是{age}，未成年，不可上网')

#多重判断练习
age = int(input('请输入您的年龄：'))
if age < 18:
    print('童工，不合法')
elif 18 <= age <= 60:
    print('合法工龄')
else:
    print('退休年龄')
print('执行完毕')

#if嵌套-坐公交车
money = input('您是否有钱：')
if money == '是':
    print('可以乘坐公交')
    set = input('车上是否有座位：')
    if set == '是':
        print('您可以坐下')
    else:
        print('您只能站着了')
else:
    print('不可以乘坐公交')