def rightrotate(arr,n,outofplace,cur):
    temp=arr[n-1]
    for i in range(cur,outofplace,cur):
        arr[i]=arr[i-1]
    arr[outofplace]=temp
    return arr

def rearrange(arr,n):
    outofplace=-1
    for index in range(n):
        if (outofplace>0):
            # if element at outOfPlace place in
            # negative and if element at index
            # is positive we can rotate the
            # array to right or if element
            # at outOfPlace place in positive and
            # if element at index is negative we
            # can rotate the array to right
            if ((arr[index]>=0 and arr[outofplace]<0)or arr[index]<0 and arr[outofplace]>=0):
                arr=rightrotate(arr,n,outofplace, index)
                if (index-outofplace>2):
                    outofplace=+2
                else:
                    outofplace=-1
            if (outofplace==-1):
                # conditions for A[index] to
                # be in out of place
                if ((arr[index]>=0 and index %2==0)or (arr[index]<0 and index %2==1)):
                    outofplace=index
        return arr

arr=[-5,-2,5,2,4,7,1,8,0,-8]
print("given array is ",arr)

print("\nReaarrange array is ",rearrange(arr,len(arr)))

