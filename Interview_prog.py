alist=[67,34,12,343,23,2]
n=len(alist)
for i in range(n):
    for j in range(i+1,n):
        if alist[i]>alist[j]:
            alist[i],alist[j]=alist[j],alist[i]
print(alist)