def solve(arr,i,j):

    if (i>j):
        return 0

    for k in range(i,j):
        temp=solve(arr,i,k)+solve(arr,k+1,j)
        ans=max(temp)

    return ans 
    