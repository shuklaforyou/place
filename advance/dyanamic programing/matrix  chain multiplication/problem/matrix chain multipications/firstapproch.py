import sys 
def solve(arr,i,j):
    if i>=j:
        return 0
    _mini=sys.maxsize
    for k in range(i,j):
        tempans=solve(arr,i,k)+ solve(arr,k+1,j) + arr[i-1]* arr[k]* arr[j]
        if tempans < _mini :
            _mini=tempans

    return _mini 

a=[40,20,30,10,30]
i=1
j=len(a)-1
print(solve(a,i,j))