#三角形左对齐
for i in range(5):
    for j in range(0,i):
        print('*',end='')
    for j in range(i,5):
        print(end='')
    print()
print('------------------')
#三角形右对齐
for i in range(5):
    for j in range(0,5-i):
        print(' ',end='')
    for j in range(5-i,5):
        print('*',end='')
    print()
print('------------------')
#三角形上下颠倒-左对齐颠倒
for i in range(5):
    for j in range(0,i):
        print(end='')
    for j in range(i,5):
        print('*',end='')
    print()
print('------------------')
#三角形上下颠倒-右对齐颠倒
for i in range(5):
    for j in range(0,i):
        print(' ',end='')
    for j in range(i,5):
        print('*',end='')
    print()
print('------------------')
#三角形-正三角形
for i in range(5):
    for j in range(0,5-i):
        print(' ',end='')
    for j in range(5-i,5):
        print('*',end=' ')
    print()
print('------------------')
#三角形-倒正三角形
for i in range(5):
    for j in range(0,i):
        print(' ',end='')
    for j in range(i,5):
        print('*',end=' ')
    print()
print('------------------')
#三角形-菱形
for i in range(5):
    if i <= 2:
        for j in range(0, 2-i):
            print(end=' ')
        for j in range(2-i, 3):
            print('*', end=' ')
        print()
    else:
        for j in range(3, i+1):
            print(end=' ')
        for j in range(i, 5):
            print('*', end=' ')
        print()

