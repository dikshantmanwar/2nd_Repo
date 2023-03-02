# alist=[67,34,12,343,23,2]
# n=len(alist)
# for i in range(n):
#     for j in range(i+1,n):
#         if alist[i]>alist[j]:
#             alist[i],alist[j]=alist[j],alist[i]
# print(alist)

##-----------------------------------
alist=[67,34,12,343,23,2]
ln=sln=alist[0]
for i in alist:
    if i > ln:
        ln=i
for i in alist:
    if i>sln and i !=ln:
        sln=i
print(sln)

