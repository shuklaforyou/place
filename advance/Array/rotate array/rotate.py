#rotate  array in clock wise 
def rotate(arr,n):
    pos=arr[n-1:] + arr[:n-1]
    return pos

arr=[1,2,3,4,5]
n=len(arr)
print(rotate(arr,n))