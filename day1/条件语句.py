# #获取年龄
# age = int(input('请输入您的年龄：'))
# #判断年龄是否大于18岁
# if age >= 18:
#     #是,可以上网
#     print('可以上网')
# #否，不可以上网，回家写作业吧
# else:
#     print('不可以上网，回家写作业吧')
# #结束
# print('关闭系统')

# # 获取年龄
# age = int(input('请输入您的年龄：'))
# # 判断年龄在0~18
# if 0 <= age < 18:
#     # 是，童工
#     print('童工')
# # 判断年龄在18~60
# elif 18 <= age <= 60:
#     # 是，合法工龄
#     print('合法工龄')
# # 判断年龄在60岁以上
# elif age > 60:
#     # 是，退休
#     print('退休')
# # 以上条件都不满足，输入错误
# else:
#     print('输入错误')

#获取钱数
money = int(input('请输入钱：'))
#判断是否有钱
if money > 0:
    #有钱，上车
    print('可以上车')
    #获取座位数
    seat = int(input('请输入座位数：'))
    #判断是否有座
    if seat > 0:
        #有座，坐着
        print('有座，可以坐下')
    #无座，站着
    else:
        print('无座，只能站着')
#没钱，无法上车
else:
    print('无法上车')

