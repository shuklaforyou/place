def findduplicate(num,n):
    num.sort()
    for i in range(1,len(num)):
        if num[i]==num[i-1]:
            return num[i]

arr=[1,3,4,2,2]
print(findduplicate(arr,len(arr)))