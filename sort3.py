#--coding:utf-8--
a=[3,2,6,8,5,1,9,4,7]

for i in range (len(a)-1):
    for j in range (i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            
print a 