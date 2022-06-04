def findmindiff(arr,n,m):
    if (m==0 or n==0):
        return 0
    arr.sort()
    if (n<m):
        return -1
    min_diff=arr[n-1]-arr[0]
    for i in range(len(arr)-m+1):
        min_diff=min(min_diff,arr[i+m-1]-arr[i])

    return min_diff

if __name__ == "__main__":
    arr=[7,3,2,4,9,15,56]
    m=3
    n=len(arr)
    print("minimum difference is,",findmindiff(arr,n,m))