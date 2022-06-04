def bsearchl(arr,n,ele):
    start=0
    end=n-1
    result1=-1
    while start<=end:
        mid = int(start + (end-start/2))
        if ele==arr[mid]:
            result1=mid
            end=mid-1
        elif ele<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return result1


def bsearchr(arr,n,ele):
    start=0
    end=n-1
    result2=-1    
    while start<=end:
        mid = int(start + (end-start/2))
        if ele==arr[mid]:
            result2=mid
            start=mid+1
        elif ele<arr[mid]: 
            end=mid-1
        else:
            start=mid+1
    return result2


def bsearch(arr,n,ele):
    return bsearchr(arr,n,ele)-bsearchl(arr,n,ele)+1

a=[2,4,10,10,10,18,20]
ele=10
n=len(a)
print(bsearch(a,n,ele))