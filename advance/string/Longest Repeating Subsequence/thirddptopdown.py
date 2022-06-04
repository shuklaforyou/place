def lrs(s1,i,j,dp):
    if i>=len(s1) or j >=len(s1):
        return 0 
    if dp[i][j]!=-1:
        return dp[i][j]
    if dp[i][j]==-1:
        if s1[i] == s1[j] and i!=j:
            dp[i][j]=1+lrs(s1,i+1,j+1,dp)
        else:
            dp[i][j]=max(lrs(s1,i+1,j,dp),lrs(s1,i,j+1,dp))

    return dp[i][j]

if __name__=="__main__":
    s1="aabb"
    dp=[[-1 for i in range(1000)]for  j in range(1000)]
    print(lrs(s1,0,0,dp))


