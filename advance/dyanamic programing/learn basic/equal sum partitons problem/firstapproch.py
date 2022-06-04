def subsetsum(arr,n,sum):
    t =([[False for i in range(sum + 1)]
            for i in range(n + 1)])
     
    # If sum is 0, then answer is true
    for i in range(n + 1):
        t[i][0] = True
         
    # If sum is not 0 and arr is empty,
    # then answer is false
    for i in range(1, sum + 1):
         t[0][i]= False
             
    # Fill the t table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<arr[i-1]:
                t[i][j] = t[i-1][j]
            if j>= arr[i-1]:
                t[i][j] = (t[i-1][j] or
                                t[i - 1][j-arr[i-1]])
     
    # uncomment this code to print table
    # for i in range(n + 1):
    # for j in range(sum + 1):
    # print (t[i][j], end =" ")
    # print()
    return t[n][sum]
         


def subset(arr,n):
    sum1=0
    for i in range(0,n):
        sum1 = sum1 + arr[i]
    sum2=int(sum1/2)
    if (sum1 %2 != 0):
        return False

    elif (sum1%2==0):
        print(subsetsum(arr,n,sum2))
    return 

arr=[1,5,11,5]
n=len(arr)
print(subset(arr,n))
