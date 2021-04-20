#打开文件
f = open('data.txt','r',encoding='UTF-8')
#对文件进行操作
text_list = f.readlines()
#关闭文件
f.close()
# 定义一个空字典，将信息存入字典
dict1 = {}
#循环遍历读取的文件内容列表
for line in text_list:
    #将每行内容后的\n去掉
    line.strip('\n')
    if line.find(',') == -1 :
        pass
    else:
        #将每行内容用逗号进行分割，形成列表
        line_list = line.split(',')
        #循环遍历列表元素
        for info in line_list:
            #将每个元素用冒号分割，第一个元素为key，第二个元素为value，存入字典
            info_list = info.split(':')
            #将信息存入字典
            dict1[info_list[0]]=info_list[1]
#读取字典中的key和value
for key,value in dict1.items():
    #判断value值如果大于18，则打印key值
    if int(value) > 18:
        print(key)