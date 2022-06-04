def minihight(arr,size,k):
    max_end=0
    min_end=0
    sum=0
    for i in range(0,size):
        if arr[i]>k:
            arr[i]=arr[i]-k
        elif arr[i]< k  :
            arr[i]=arr[i]+k
        else :
            arr[i]=arr[i]+k
    # for i in range(size):
    #     if max_end <arr[i]:
    #         max_end=arr[i]

    #     elif min_end > arr[i]:
    #         min_end=arr[i]
    #     else:
    #         pass
    arr.sort()
    print(arr)
    max_end=arr[n-1]
    min_end=arr[1]
    sum=max_end-min_end
    return sum

k=2
arr=[1,5,8,10]
n=len(arr)
print(minihight(arr,n,k))