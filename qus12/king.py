def last_lines(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        return lines[::-1]
lines=last_lines('main.txt')
for i in lines:
    i=i.replace("\n","")
    print(i)
