dp=[[0 for i in range(1000)]for j in range(1000)]

def flss(x,m,n):
    if dp[m][n]!=-1:
        return dp[m][n]
    if m==0 or n==0:
        dp[m][n]=0
        return dp[m][n]
    
    if x[m-1]==x[n-1] and m!=n:
        dp[m][n]=flss(x,m-1,n-1)+1
        return dp[m][n]

    dp[m][n]= max(flss(x,m-1,n),flss(x,m,n-1))
    return dp[m][n]

if __name__=="__main__":
    str="aabb"
    m=len(str)

dp=[[-1 for i in range(1000)]for j in range(1000)]
print(flss(str,m,m))

