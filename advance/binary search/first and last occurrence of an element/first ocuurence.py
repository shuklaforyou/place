def bsearch(arr,n,ele):
    start=0
    end=n-1
    result=-1
    while start<=end:
        mid = int(start + (end-start/2))
        if ele==arr[mid]:
            result=mid
            end=mid-1
        elif ele<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return result


a=[2,4,10,10,10,18,20]
ele=10
n=len(a)
print(bsearch(a,n,ele))