def getodd(arr,n):
     for i in range(0,n):
         count=0
         for j in range(0,n):
             if arr[i]==arr[j]:
                 count+=1

             if ( count % 2 !=0):
                return arr[i]

     return -1

arr=[2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 ]
n= len(arr)
print(getodd(arr,n))
