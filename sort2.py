#--coding:utf-8--
list=[3,5,7,9,1,2,4,6,8]
for i in range(len(list)):
    for j in range(i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print list
