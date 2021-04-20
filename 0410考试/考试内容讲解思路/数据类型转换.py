#如何实现[‘1’,’2’,’3’]变成[1,2,3] ?
list1 = ['1','2','3']
list2 = []
for i in list1:
    j = int(i)
    list2.append(j)

print(list2)