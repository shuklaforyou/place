def knapSack(leng, price, n,N):
    t = [[0 for x in range(n + 1)] for x in range(N + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for j in range(N + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif leng[i-1] <= j:
                t[i][j] = max(price[i]
                          + t[i-1][j-leng[i-1]], 
                              t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
 
    return t[n][j]
 
leng = [1,2,3,4,5,6,7,8]
wt = [1,5,8,5,10,17,17,20]
N = 8
n = len(leng)
print(knapSack(leng,wt, n, N))
 