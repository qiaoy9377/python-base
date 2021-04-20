#开发一个注册系统
'''
页面：
[{name:xxx,age:xxx},xxx]
----------------
*   1-新增用户
*   2-查询用户
*   3-删除用户
----------------
功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
功能2：查询学生信息
功能3：删除学生信息
'''

#学生信息列表
student_info = [
    {'name':'Tom','age':18,'gender':'男'},
    {'name':'Rose','age':19,'gender':'女'},
    {'name':'小红','age':20,'gender':'女'},
]

#定义显示功能界面函数
def main_func():
    print('----------------')
    print('*   1-新增用户')
    print('*   2-查询用户')
    print('*   3-删除用户')
    print('----------------')
    #声明全局变量
    global choice
    choice = int(input('请输入您要进行的操作（1-新增用户，2-查询用户，3-删除用户）：'))

#定义新增学生信息函数
def add_student():
    #输入要添加的学生信息
    add_name = input('请输入您要添加的学生姓名：')
    add_age = input('请输入您要添加的学生年龄：')
    add_gender = input('请输入您要添加的学生性别：')
    # 声明全局变量，修改才会生效
    global student_info
    #循环找学生信息
    for i in student_info:
        #判断学生姓名是否存在
        if add_name in i['name']:
            #是，打印该学生已存在
            print('该学生已存在')
            break
    else:
        #否，添加该学生信息，提示添加成功
        student_info.append({'name':add_name,'age':add_age,'gender':add_gender})
        print('添加成功')
        print(student_info)
    #调用功能显示界面
    main_func()
    # 选择功能操作
    select_operatin()

#定义查询学生信息函数
def search_student():
    #输入查询的学生姓名
    search_name = input('请输入您要查询的学生姓名：')
    #循环遍历学生信息
    for i in student_info:
        #判断学生姓名是否在列表中
        if search_name in i['name']:
            #存在，打印该学生信息
            print(i)
            break
    else:
        #不存在，给出提示信息
        print('该学生信息不存在')
    #返回功能界面
    main_func()
    # 选择功能操作
    select_operatin()

#定义删除学生信息函数
def del_student():
    #输入删除学生姓名
    del_name = input('请输入您要删除的学生姓名：')
    # 声明全局变量，修改才会生效
    global student_info
    #循环遍历学生信息
    for i in student_info:
        #判断该学生是否存在
        if del_name == i['name']:
            #存在，则删除，并给出提示信息
            student_info.remove(i)
            print('删除成功')
            print(student_info)
            break
    else:
        #不存在，给出提示信息
        print('该学生信息不存在')
    main_func()
    # 选择功能操作
    select_operatin()

#功能操作选择判断
def select_operatin():

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        del_student()
    else:
        print('选择不存在，退出系统')

#显示功能界面
main_func()
#选择功能操作
select_operatin()
