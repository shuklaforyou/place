def mergsort(arr1,n,arr2,m):
    for i in range(m):
        arr1.append(arr2[i])
    arr1.sort()
    return arr1


n=4
arr1=[1,3,5,7]
m=5
arr2=[0,2,6,8,9]

print(mergsort(arr1,n,arr2,m))