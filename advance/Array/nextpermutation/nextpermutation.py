def reverse(arr,start):
    i=start
    j=len(arr)-1
    while (i<j):
        swap(arr,i,j)
        i+=1
        j-=1
    return 

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    return


def permnutation(arr,n):
    i=n-2
    while (i>=0  and arr[i+2]<=arr[i]):
        i-=1
        if (i>=0):
            j=n-1
            while (arr[j]<=arr[i]):
                j -=1

            swap(arr,i,j)

        reverse(arr,i+1)
    return arr 


arr=[9,5,4,3,1]
print(permnutation(arr,len(arr)))
#not working code 
#error is out of range line 19
