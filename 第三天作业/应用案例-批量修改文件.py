#批量修改文件名，即可添加指定字符串，又能删除指定字符串
'''
步骤思路：
1、获取需要修改的文件路径
2、获取文件列表
3、循环取文件列表内容进行rename
'''
#导入os模块
import os

def rename_multi_file():
    #获取文件路径
    file_path = input('请输入您要修改发文件路径：')
    #输入想要修改的方式
    menthod = int(input('请输入您想要进行的操作（1-添加、2-删除）：'))
    #输入想要添加或者删除的字符串
    content = input('请输入您想要添加或删除的字符：')
    #获取文件列表
    file_list = os.listdir(file_path)
    #改变默认目录
    os.chdir(file_path)
    #判断用户选择的操作
    if menthod == 1:
        #循环取文件进行重命名
        for file in file_list:
            # os.rename(file_path+file,file_path+content+file)   可以直接加上文件路径进行重命名
            os.rename(file, content + file)
        #打印重命名后的文件列表
        print(os.listdir(file_path))
    elif menthod == 2:
        # 循环取文件进行重命名
        for file in file_list:
            if content in file:
                content_index = file.find(content)
                content_len = len(content)
                os.rename(file, file[:content_index] + file[content_index+content_len:])
        # 打印重命名后的文件列表
        print(os.listdir(file_path))

    else:
        print('操作不存在')

rename_multi_file()