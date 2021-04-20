#三角形不同样子--右对齐
i = 1
while i <= 5:
    j = 5
    while j > i:
        print(' ',end='')
        j -= 1
    else:
        while 1<= j <=i :
            print('*', end='')
            j -= 1
    print()
    i+=1

#三角形不同样子--上下颠倒
#1、左对齐上下颠倒
i = 1
while i <= 5:
    j = 5
    while j >= i:
        print('*',end='')
        j -= 1
    print()
    i += 1
#2、右对齐上下颠倒
i = 5
while i >= 1:
    j = 5
    while j > i:
        print(' ',end='')
        j -= 1
    else:
        while 1 <= j <= i:
            print('*',end='')
            j -= 1
    print()
    i -= 1

#三角形不同样子--正三角形
i = 1
while i <= 5:
    j = 5
    while j > i:
        print( end=' ')
        j -= 1
    else:
        while 1 <= j <= i:
            print('*',end=' ')
            j -= 1
    print()
    i += 1


#三角形的不同样子--菱形
#
i = 1
k = 5
k1 = (k+1)/2
while i <= k:
    j = k1
    if i <= k1:
        while j > i:
            print(end=' ')
            j -= 1
        else:
            while 1 <= j <= i:
                print('*', end=' ')
                j -= 1
    else:
        while j < i:
            print(end=' ')
            j += 1
        else:
            while k >= j >=i:
                print('*', end=' ')
                j += 1
    print()
    i += 1

