num1 = 10
num2 = 20
num3 = num1+num2
num4 = num1-num2
num5 = num1*num2
num6 = num1/num2
num7 = num1//num2
num8 = num1%num2
num9 = num1**3
num10 = (num1+num2)*2
print(num3,num4,num5,num6,num7,num8,num9,num10)

num1 = '10'
num2 = '20'
num3 = num1+num2
num4 = num1*5
print(num3)
print(num4)

num1,float1,str1 = 10,15.5,'hello world'
print(num1)
print(float1)
print(str1)

a=b=1
print(a)
print(b)

a = 100
a += 1
print(a)

b = 2
b *= 3
print(b)

c = 10
c += 1+2   #先算运算符右侧1+2=3，推导得出c += 3
print(c)

a = 7
b = 5
print(a == b)
print(a > b)
print(a < b)
print(a != b)
print(a <= b)
print(a >= b)

a = 1
b = 2
c = 3
print((a<b)and (b<c))
print((a>b)and (b<c))
print((a>b)or (b<c))
print(not(a>b))

a = 0
b = 1
c = 2
print(a and b)
print(b and a)
print(a and c)
print(b and c)
print(c and b)

print(a or b)
print(a or c)
print(b or c)