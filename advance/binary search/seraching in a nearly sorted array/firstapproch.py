def searh(arr,l,r,x):
    if (r >= l):
         
        mid = int(l + (r - l) / 2)
   
        if (arr[mid] == x): return mid
        if (mid > l and arr[mid - 1] == x):
            return (mid - 1)
        if (mid < r and arr[mid + 1] == x):
            return (mid + 1)

        if (arr[mid] > x):
            return searh(arr, l, mid - 2, x)

        return searh(arr, mid + 2, r, x)
 

    return -1
 

arr = [5,10,30,20,40]
n = len(arr)
x = 30
result = searh(arr, 0, n - 1, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)