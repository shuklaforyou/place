import sys

t=[[-1 for i in range(11)]for i in range(51)]

def solve(e,f):
    if f==0 or f==1:
        return 1
    if e==1:
        return f
    if t[e][f]!=-1:
        return t[e][f]
    mn=sys.maxsize
    for k in range(1,f):
        if t[e-1][k-1]!=-1:
            low=t[e-1][k-1]
        else:
            low=solve(e-1,k-1)
        if t[e][f-k]!=-1:
            high=t[e][f-k]
        else:
            high=solve(e,f-k)
            t[e][f-k]=high
        temp=1+ max(low,high)
        mn=min(mn,temp)
    t[e][f]=mn
    return t[e][f]


e=3
f=5
print(solve(e,f))