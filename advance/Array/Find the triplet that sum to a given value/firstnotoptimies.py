def find3numbers(a,arr_size,sum):
    for i in range(0,arr_size-2):
        for j in range(i+1,arr_size-1):
            for k in range(j+1,arr_size):
                if a[i] +a[j] + a[k] == sum:
                    print("triplet is ,",a[i],a[j],a[k])
                    return True
    return 

a=[1,4,45,6,10,8]
arr_size=len(a)
sum=22
print(find3numbers(a,arr_size,sum))