# l=[1,2,3,4,5,6,7]
# l.pop(2)
# print(l)

l=[1,2,3,4,5,6,7]
index=int(input("enter index postion:"))
l=l[:index]+l[index+1:]
print(l)