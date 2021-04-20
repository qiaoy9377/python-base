#猜拳游戏-石头、剪刀、布
#判断输赢：1、玩家获胜：石头——>剪刀；剪刀——>布；布——>石头；2、平局：玩家出拳和电脑出拳相同；3、电脑获胜
#引入随机数：0-石头；1-剪刀；2-布；
# 1、出拳：玩家输入出拳，电脑随机出拳；2、判断输赢
import random
#玩家输入
player = int(input('请出拳(0-石头；1-剪刀；2-布)：'))
#电脑随机生成
computer = random.randint(0,2)
print(computer)
#平局
if player == computer:
    print('平局')
#玩家获胜的情况
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家获胜')
#电脑获胜的情况
else:
    print('电脑获胜')

#三目运算
#条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
a = 2
b = 1

c = a if a > b else b
print(c)

