#打开文件
f = open('data.txt','r')
#循环读取文件
while True:
    #读取每行内容
    text = f.readline()
    #将内容以逗号进行切割
    list1 = text.split(',')
    #循环遍历切割后每个元素
    for i in list1:
        #寻找冒号的下标
        index = i.find(':')
        #如果没有找到下标就不执行操作
        if index == -1:
            pass
        #如果找到冒号下标
        else:
            #将字符串以冒号进行切片，得出年龄
            age = int(i[index+1:])
            #print(age)
            #判断年龄是否大于18
            if age > 18:
                #如果大于18则切片冒号前面的姓名
                print(i[:index])
    #print(text)
    #如果读取不到文件内容就跳出循环
    if text == '':
        break
