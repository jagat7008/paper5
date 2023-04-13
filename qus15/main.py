lst = ['data','science','artificial', 'intelligence'] 
dct = {'data': 5, 'science': 3, 'machine': 1, 'learning': 8}
res={}
for i in lst:
    if i in dct:
        res.update({i:dct[i]})
    else:
        res.update({i:len(i)})
print(res)
