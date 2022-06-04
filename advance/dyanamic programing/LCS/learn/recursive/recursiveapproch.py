def lcs(x,y,n,m):
    if n== 0 or m ==0:
        return 0
    if (x[n-1]==y[m-1]):
        return 1+lcs(x,y,n-1,m-1)
    else:
        return max(lcs(x,y,n,m-1),lcs(x,y,n-1,m))


x=['a','b','c','d','g','h']
y=['a','b','e','d','f','h','r']
n=len(x)
m=len(y)
print(lcs(x,y,n,m))