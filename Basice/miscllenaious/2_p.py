def UniqueNumber2(arr,n):
    sums=0
    for i in range(0,n):
        sums=(sums ^ arr[i])
    sums=(sums & -sums)
    sum1=0
    sum2=0
    for i in range(0,len(arr)):
        if (arr[i] & sums) >0:
            sum1 =(sum1 ^ arr[i])
        else:
            sum2=(sum2 ^ arr[i])

    print("the non-repeating elements are ",sum1 ,"and",sum2)

if __name__ =="__main__":

    arr=[2,3,7,9,11,2,3,11]
    n=len(arr)
    UniqueNumber2(arr,n)

#Find the two non-repeating elements
#in an array of repeating elements/ Unique Numbers 2
