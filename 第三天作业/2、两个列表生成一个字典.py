#有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
name_list = ['张三','李四','TOM','Rose','xiaoming','xiaohong']
age_list = [18,19,20,19,21,18]
#字典推导式
student_dict = {name_list[i]:age_list[i] for i in range(len(name_list))}
print(student_dict)

#for循环
#创建一个空字典
student_dict1 = {}
#循环下标，将数据插入字典
for i in range(len(name_list)):
    student_dict1[name_list[i]] = age_list[i]
print(student_dict1)

#while循环
#创建一个空字典
student_dict2 = {}
#循环变量-列表数据下标
i = 0
#循环判断--判断下标是否在列表长度范围内
while i < len(name_list):
    #循环体，将列表内容插入字典
    student_dict2[name_list[i]] = age_list[i]
    #循环变量发生变化
    i += 1
print(student_dict2)
