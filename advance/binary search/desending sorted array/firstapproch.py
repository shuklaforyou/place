def bsearch(arr,n,ele):
    start=0
    end=n-1
    while start<=end:
        mid = int(start + (end-start/2))
        if ele==arr[mid]:
            return mid
        elif ele<arr[mid]:
            start=mid+1
        else:
            end=mid-1



a=[20,17,15,14,13,12,10,9,8,4]
ele=4
n=len(a)
print(bsearch(a,n,ele))