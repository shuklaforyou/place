def find3numbers(a,arr_size,sum):
    for i in range(0,arr_size-1):
        s=set()
        curr_sum=sum-a[i]
        for j in range(i+1,arr_size):
            if (curr_sum -a[j]) in s:
                print("triplate is ,",a[i],a[j],curr_sum-a[j])
                return True
            s.add(a[j])
    return False 

a=[1,4,45,6,10,8]
arr_size=len(a)
sum=22
print(find3numbers(a,arr_size,sum))