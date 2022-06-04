# n=input("length of arry :-")
# arr=list(map(int,input().split()))
# k=int(input("which pogstion :-"))

# arr.sort()
# print(arr[k-1])

def kthSmallest(self,arr, l, r, k):
       def uday(arr,l,r,n,k):
           Counter=0
           arr.sort(reverse=False)
           for i in range(n):
               if arr[i]<=arr[r]:
                   Counter+=1
               l+=1
               if Counter==k:
                   return arr[i]
       return uday(arr,l,r,k) #n also there in 

#both are true
