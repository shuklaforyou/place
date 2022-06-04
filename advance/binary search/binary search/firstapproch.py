def bsearch(arr,n,ele):
    start=0
    end=n-1
    while start<=end:
        mid = int(start + (end-start/2))
        if ele==arr[mid]:
            return mid
        elif ele<arr[mid]:
            end=mid-1
        else:
            start=mid+1



a=[1,2,3,4,5,6,7,8,9,10]
ele=2
n=len(a)
print(bsearch(a,n,ele))