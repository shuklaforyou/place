def subarray(arr,n):
    n_sum=0
    s=set()
    for i in range(n):
        n_sum+=arr[i]
        #print(n_sum)
        if n_sum==0 or n_sum in s:
            return True
        s.add(n_sum)
        #print(s)
    
    return False


arr=[4,2,-3,1,6]
n=len(arr)
if subarray(arr,n)==True:
    print("Yes")
else:
    print("No")

print(subarray(arr,n))
