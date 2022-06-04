import sys 
def subsetsum(arr,n):
    sum1=0
    for i in range(0,n):
        sum1 = sum1 + arr[i]
    sum=sum1
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
    diff = sys.maxsize
    for j in range(sum//2,-1,-1):
         if t[n][j] == True:
            diff=sum1-2*j
            break
 
    return diff
         
a = [3, 1, 4, 2, 2, 1]
n = len(a)
 
print("The minimum difference between "
      "2 sets is ",subsetsum(a, n))
 


   
    
arr=[1,5,11,5]
n=len(arr)
print(subsetsum(arr,n))
