a=[8,9,10,"f",4,5,"d"]
output=[]
for element in a:
    if type(element)==int:
        output.append(element**2)
    elif type(element)==str:
        output.append(element*2)
print(output)