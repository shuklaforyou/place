import sys
def isplaindrome(s,i,j):
    b=str(s[::-1])
    if b == s:
        return  True
    else:
        return  False
    

def solve(a,i,j):
    if (i>=j):
        return 0
    if isplaindrome(a,i,j)==True:
        return 0
    ans=sys.maxsize
    for k in range(i,j):
        temp= solve(a,i,k)+ solve(a,k+1,j) +1
        ans=min(ans,temp)

    return ans

def mcm(a,n):
    i=1
    j=n-1
    return solve(a,i,j)

a="nitin"
n=len(a)
print(mcm(a,n))
    