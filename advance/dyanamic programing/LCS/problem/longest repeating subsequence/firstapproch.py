def lcs(x,y,m,n):
    t=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif x[i-1] == y[j-1] and i!=j:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])

    return t[m][n]

def lrp(a):
    b=a
    m=len(a)
    n=len(b)
    return lcs(a,b,m,n)

a="AABEBCDD"
print(lrp(a))