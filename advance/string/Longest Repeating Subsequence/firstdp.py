def flss(str):
    n=len(str)
    dp = [[ 0 for i in range(n+1)]for j in range(n+1) ]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if str[i-1]==str[j-1] and i !=j:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])

    return dp[i][j]

if __name__=="__main__":
    str="aabb"
    print(flss(str))
    