def lcs(X,Y,m,n):
    t=[[0 for k in range(n+1)] for l in range(m+1)]
    result = 0
    for i in range(m+1):
        for j in range(n+1):
            if i== 0 or j== 0:
                t[i][j] = 0

            elif X[i-1] == Y[j-1]:
                t[i][j] = t[i-1][j-1]+1
                result = max(result, t[i][j])

            else:
                t[i][j] = 0

    return result

x="ABCDE"  
y="ABFCE"
m=len(x)
n=len(y)
print(lcs(x,y,m,n))    