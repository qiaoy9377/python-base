#定义一个用户信息表
list1 = [
    {'name':'Tom','password':12345},
    {'name':'Rose','password':111111},
    {'name':'小红','password':000000}
]
#功能界面函数
def fun1():
    print('-' * 20)
    print('注册系统')
    print('用户名')
    print('密码')
    print('注册')
    print('-' * 20)

#注册功能
def register():
    #输入用户名、密码
    name = input('请输入用户名：')
    password = input('请输入密码：')
    #声明全局变量
    global list1
    #循环遍历用户信息表
    for i in list1:
        #判断用户是否存在
        if name == i['name']:
            #如果存在则提示信息已注册
            print('用户信息已注册')
            break
    else:
        #如果不存在则添加用户信息
        dict1 = {}
        dict1['name'] = name
        dict1['password'] = password
        list1.append(dict1)
        print('注册成功')
        print(list1)

while True:
    fun1()
    num =input('请输入您要进行的操作（1-注册，2-退出系统）序号：')
    if num == '1':
        register()
    elif num == '2':
        break
    else:
        print('输入错误，请重新输入')

