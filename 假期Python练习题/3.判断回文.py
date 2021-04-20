#实现函数is_palindrome,判断参数string是否为回文，所谓回文，就是左右对称的字符串
def is_palindrome(string):
    '''
    判断字符串string是回文
    :param string: 需要判断的字符串
    :return: 布尔值true false
    '''
    l = len(string)
    string1 = string[::]
    string2 = string[::-1]
    if string1 == string2:
        return True
    else:
        return False

print(is_palindrome('abcddcba'))
print(is_palindrome('pythonohtyp'))
print(is_palindrome('bookkob'))