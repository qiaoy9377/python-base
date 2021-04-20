#实现函数get_max_socre,执行程序，最终输出：英语 98
dic = {
    '语文':90,
    '数学':97,
    '英语':98
}

def get_max_score(score_dic):
    '''
    返回学生考试成绩的最高分的科目和分数
    :param score_dic: 学生成绩字典
    :return: 最高分的科目和分数
    '''
    #创建一个科目列表
    course_list = [course for course in dic.keys()]
    #将第一科目进行赋值
    max_course = course_list[0]
    #循环取科目
    for course in course_list:
        #判断当前科目分数是否大于目前最高分的科目
        if dic[course] > dic[max_course]:
            #如果大于则进行最高分科目和最高分的赋值
            max_course = course
            max_score = dic[course]
    #返回最高分科目和成绩
    return max_course,max_score

course,score = get_max_score(dic)
print(course,score)