def find3numbers(a,arr_size,sum):
    a.sort()
    for i in range(0,arr_size):
        l=i+1
        r=arr_size-1
        while (l<r):
            if a[i] + a[l]+a[r] ==sum:
                print("triplet is",a[i],a[l],a[r])
                return True
            elif (a[i] +a[l] + a[r] < sum):
                l+=1
            else:
                r-=1
    return False

a=[1,4,45,6,10,8]
arr_size=len(a)
sum=22
print(find3numbers(a,arr_size,sum))