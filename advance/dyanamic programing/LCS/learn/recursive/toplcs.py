def lcs(X,Y,m,n):
    t=[[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i== 0 or j== 0:
                t[i][j] = 0
            elif X[i-1] == Y[j-1]:
                t[i][j] = t[i-1][j-1]+1

            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])

    return t[m][n]

x="ABCDGF"  
y="ACBCF"
m=len(x)
n=len(y)
print(lcs(x,y,m,n))    