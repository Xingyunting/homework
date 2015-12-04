＃－－coding：utf-8--
list2=[3,5,7,2,9,4,6,8,1]

for i in range(0,len(list2)):
    min=i
    for j in range (i+1,len(list2)):
        if list2[j]<list2[min]:
            min=j
    list2[i],list2[min]=list2[min],list2[i]#swap
    
print list2
#选择排序