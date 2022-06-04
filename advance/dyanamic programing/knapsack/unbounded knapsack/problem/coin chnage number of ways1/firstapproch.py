def coinone(arr,sum,n):
    t= [[0 for x in range(sum+1)] for x in range(n+1)]


    for i in range(n+1):
        t[i][0]=1

    for i in range(sum+1):
        t[0][i]=0

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j] + t[i][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]

    return t[n][sum]

arr=[1,2,3]
sum=5
n=len(arr)
print(coinone(arr,sum,n))