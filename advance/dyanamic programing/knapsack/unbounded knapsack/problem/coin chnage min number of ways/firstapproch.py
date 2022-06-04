import sys

def coinone(arr,sum,n):
    t= [[0 for x in range(sum+1)] for x in range(n+1)]

    max_int = sys.maxsize


    for i in range(1,n+1):
        t[i][0]=0

    for i in range(sum+1):
        t[0][i]=1
    
    p=1
    for j in range(1,sum+1):
        if j%arr[0] == 0:
            t[p][j]=int(j/arr[0])
        else:
            t[p][j]=max_int - 1
    

    for i in range(2,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]= min(t[i-1][j] , 1 + t[i][j-arr[i-1]])
            else:
                t[i][j]=t[i-1][j]

    return t[n][sum]

arr=[1,2,3]
sum=5
n=len(arr)
print(coinone(arr,sum,n))