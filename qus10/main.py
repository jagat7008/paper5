lst=[12,3,43,5,65,65,87]
for i in range(len(lst)-1,0,-1):
    for j in range(i):
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)