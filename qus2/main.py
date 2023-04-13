list_1=[1,2,3,4,3,2,1,4,3,5,5,6,7,7]
list_2=[]
for i in list_1:
    if i not in list_2:
        list_2+=[i]
print(list_2)