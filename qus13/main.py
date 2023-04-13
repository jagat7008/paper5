def twonos():
    try:
        x=int(input("enter  1st nos:"))
        y=int(input("enter 2nd nos"))
        mx=max(x,y)
        mn=min(x,y)
        ans=mx/mn
    except ValueError as e:
        print("input should be of integer type only.....")
    except ZeroDivisionError as e:
        print("cannot devide anything by zero")
    else:
        print(ans)
# while 1:
twonos()