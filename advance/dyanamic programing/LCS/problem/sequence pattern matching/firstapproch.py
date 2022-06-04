def lcs(x,y,m,n):
    t=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif x[i-1] == y[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])

    return t[m][n]
def spm(a,b):
    m=len(a)
    n=len(b)
    wel=lcs(a,b,m,n)
    #print(wel)
    if wel == len(a):
        return True
    else:
        return False

a="AXY"
b="ADXCPY"
print(spm(a,b))