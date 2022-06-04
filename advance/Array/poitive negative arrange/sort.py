# approch 1
# partition process of quicksort. 
def rearrange(arr,n):
    j=0
    for i in range(0,n):
        if (arr[i]<0):
            temp=arr[i]
            print(temp)
            arr[i]=arr[j]
            print(arr[i])
            arr[j]=temp
            print(arr[j])
            j=j+1
            print(j)
    print(arr)


arr=[-1,2,-3,4,5,6,-7,8,9]
n=len(arr)
rearrange(arr,n)
