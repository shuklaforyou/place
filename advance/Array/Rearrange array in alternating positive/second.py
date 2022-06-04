def rearrange(arr,n):
    arr.sort()
    i,j=1,1
    while j<n:
        if arr[j]>0:
            break
        j +=1
    while  (arr[i]<0) and (j<n):
        #swapping
        arr[i],arr[j]=arr[j],arr[i]
        #increment by 2 
        # because a negative number is followed by  a positve
        i +=2
        j +=1

    return arr

arr=[-5,-2,5,2,4,7,1,8,0,-8]

ans= rearrange(arr,len(arr))
for num in ans:
    print(num,end=" ")
