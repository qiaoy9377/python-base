#需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能（备份文件名为xx[备份]后缀，如：test[备份].txt）
'''
1、输入要备份的文件
2、获取文件名
3、修改文件名
4、打开文件
5、将原文件内容写入新文件
6、关闭文件
'''


def creat_file():
    # 用户输入想要备份的文件
    old_file = input('请输入您要备份的文件：')
    #获取文件名，拆解文件名和后缀，需要找到'.'的下标
    point_index = old_file.rfind('.')
    #判断输入的文件格式是否正确
    if 0 < point_index < len(old_file)-1:
        #旧文件名
        old_file_name = old_file[:point_index]
        #旧文件后缀
        old_file_extension = old_file[point_index:]
        #拼接新文件名，并创建文件
        global new_file
        new_file = old_file_name+'[备份]'+old_file_extension
        new_f = open(new_file,'ab+')

        #打开文件
        old_f = open(old_file,'rb+')
        # 写入文件内容
        #方法一：for循环readlines列表写入
        '''
        list1 = old_f.readlines()
        for i in list1:
            new_f.write(i)
        '''
        #方法二：直接读取旧文件，写入新文件
        '''
        text = old_f.read()
        new_f.write(text)
        '''
        #方法三：循环读取旧文件内容，写入新文件
        while True:
            #循环取旧文件的1024个字节
            text = old_f.read(1024)
            #判断取到的内容长度，如果等于0代表取完了，就跳出
            if len(text) == 0:
                break
            #否则将取到的内容写入新文件
            new_f.write(text)
        #关闭文件
        old_f.close()
        new_f.close()
    else:
        print('文件名输入错误')

creat_file()



