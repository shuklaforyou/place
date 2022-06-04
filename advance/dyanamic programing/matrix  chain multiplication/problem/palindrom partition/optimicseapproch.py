import sys
def isplaindrome(s,i,j):
    if i==j:
        return True
    if i>j:
        return True
    while (i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True    
        
    

t=[[-1 for i in range(100)]for j in range(100)]

def solve(a,i,j):
    if (i>=j):
        return 0
    if isplaindrome(a,i,j)==True:
        return 0
    ans=sys.maxsize
    for k in range(i,j):
        if (t[i][k]!=1):
            left=t[i][k]
        else:
            left=solve(a,i,k)
            t[i][k]=left
        if(t[k+1][j]!=-1):
            right=t[k+1][j]
        else:
            right=solve(a,i,j)
            t[k+1][j]=right
        temp=1+left+right
        ans=min(ans,temp)

    t[i][j]=ans
    return t[i][j]

def mcm(a,n):
    i=0
    j=n-1
    return solve(a,i,j)


a="nitin"
n=len(a)
print(mcm(a,n))