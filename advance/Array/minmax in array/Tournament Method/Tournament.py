def getminmax(low,high,arr):
    arr_max=arr[low]
    arr_min=arr[low]

    #if there is only one element
    if low==high:
        arr_max=arr[low]
        arr_max=arr[low]
        return (arr_max,arr_min)

    #if there is two element
    elif high == low+1:
        if arr[low]>arr[high]:
            arr_max=arr[low]
            arr_min=arr[high]
        else:
            arr_max=arr[high]
            arr_min=arr[low]
        return (arr_min,arr_max)
    else:
        # IF THERE IS MORE THAN TWO ELEMENT
        mid=int((low+high) / 2)
        arr_max1,arr_min1=getminmax(low,mid,arr)
        arr_max2,arr_min2=getminmax(mid+1,high,arr)

    return (max(arr_max1,arr_max2),min(arr_min1,arr_min2))

arr=[100,11,445,1,330,3000]
high=len(arr)-1
low=0
arr_max ,arr_min=getminmax(low,high,arr)
print("minimum elemant is",arr_min)
print("maxmum elemant is",arr_max)

#not working code
