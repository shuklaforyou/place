import sys 
def countsubset(arr,diff,n):
    sum1= 0
    sum_arr=sum(arr)
    sum1=diff+sum_arr/2
    sum2=int(sum1)
    return subsetsum(arr,n,sum2)

def subsetsum(arr,n,sum):
    t =([[0 for i in range(sum + 1)]
            for i in range(n + 1)])
     
    # If sum is 0, then answer is true
    for i in range(n + 1):
        t[i][0] = 1
         
    # If sum is not 0 and arr is empty,
    # then answer is false
    for i in range(1, sum + 1):
         t[0][i]= 0
             
    # Fill the t table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<arr[i-1]:
                t[i][j] = t[i-1][j]
            if j>= arr[i-1]:
                t[i][j] = (t[i-1][j] +
                                t[i - 1][j-arr[i-1]])
     
    # uncomment this code to print table
    # for i in range(n + 1):
    # for j in range(sum + 1):
    # print (t[i][j], end =" ")
    # print()
    return t[n][sum]

arr=[1,1,2,3]
diff=1
n=len(arr)
print(countsubset(arr,diff,n))


#same code for anothre questions