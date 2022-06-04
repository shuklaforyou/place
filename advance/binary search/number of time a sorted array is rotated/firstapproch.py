

def bsearch(arr,n):
    start=0
    end=n-1
    # print(mid,next,prev)
    while start<=end:
        mid=int(start+end-start/2)
        next=mid+1%n
        prev=mid-1+n%n 
        if arr[mid]<=arr[prev] and arr[mid]<=arr[next]:
            return mid
        if arr[start]<=arr[mid]:
            start=mid+1
        elif arr[mid]<=arr[end]:
            end=mid-1


arr=[11,12,15,18,2,5,6,8]
n=len(arr)
print(bsearch(arr,n))