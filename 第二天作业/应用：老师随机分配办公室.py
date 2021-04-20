#导入随机数模块
import random
#定义列表
teacher_list = ['老师1','老师2','老师3','老师4','老师5','老师6','老师7','老师8']
room_list = [[],[],[]]
#遍历tacher列表
for teacher in teacher_list:
    #生成房间列表的随机下标
    i = random.randint(0,2)
    #print(i)
    #将老师添加到随机下标代表的房间列表
    room_list[i].append(teacher)
#打印房间列表
print(room_list)