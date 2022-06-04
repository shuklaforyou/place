def dublicatefind(arr,n):
    seen=set()
    for ar in arr:
        if  ar in seen:
            return ar
        seen.add(ar)

arr=[1,3,4,2,2]
print(dublicatefind(arr,len(arr)))
