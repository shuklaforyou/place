import sys
def solve(e,f):
    if f==0 or f==1:
        return 1
    if e==1:
        return f
    mn=sys.maxsize
    for k in range(1,f):
        temp=1+ max(solve(e-1,k-1),solve(e,f-k))
        mn=min(mn,temp)

    return mn


e=3
f=5
print(solve(e,f))