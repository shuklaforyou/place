def lcs(x,y,m,n):
    t=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif x[i-1]==y[j-1]:
                t[i][j]=t[i-1][j-1] +1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
            
    return t[m][n]

def lcss(x,y):
    m=len(x)
    n=len(y)
    return m+n-lcs(x,y,m,n)

a="AGGTAB"
b="GXTXAYB"
print(lcss(a,b)) 