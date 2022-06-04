def floorSearch(arr, low, high, x):
 
    if (low > high):
        return -1

    if (x >= arr[high]):
        return high
 
    
    mid = int((low + high) / 2)

    if (arr[mid] == x):
        return mid

    if (mid > 0 and arr[mid-1] <= x
                and x < arr[mid]):
        return mid - 1

    if (x < arr[mid]):
        return floorSearch(arr, low, mid-1, x)
 

    return floorSearch(arr, mid + 1, high, x)
 
 

arr = [1, 2, 4, 6, 10, 12, 14]
n = len(arr)
x = 7
index = floorSearch(arr, 0, n-1, x)
 
if (index == -1):
    print("Floor of", x, "doesn't exist\
                    in array ", end = "")
else:
    print("Floor of", x, "is", arr[index])