def fectorial(n):
    p=n+1
    arr=[0]*p
    fact=1
    for i in range(0,p):
        arr[i]=i
    for m in range(1,p):
        fact=arr[m]*fact
    return fact

n=10
print(fectorial(n))

#timecomplexcity O(n^2)
#Sapce complexity O(n)
