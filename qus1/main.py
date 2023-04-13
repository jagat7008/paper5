def cal_second_large(arr):
    send_large=arr[0]
    large=arr[0]
    for i in  range(len(arr)):
        if arr[i]>large:
            large=arr[i]
    for i in range(len(arr)):
        if arr[i]>send_large and arr[i]!=large:
            send_large=arr[i]
    return send_large
print(cal_second_large([1,2,3,4,5,6,7]))
