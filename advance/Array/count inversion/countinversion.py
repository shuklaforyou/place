def inversionCount(self,arr, n):
       # Broken coder
       temp_arr=[0]*n
       return(self.mergeSort(arr,temp_arr,0,n-1))
       # just apply concept of merge sort with small modification

   #step 1: count inversion left side of arr(mergesort function)
   #step 2: count inversion remaining part array
   #step 3: merge them and return(inverion)
   
   
def mergeSort(self,arr,temp_arr,low,high):
    res=0
    if(low<high):
        mid=(high+low)//2
        res+= self.mergeSort(arr,temp_arr,low,mid)
        res+=self.mergeSort(arr,temp_arr,mid+1,high)
        res+=self.merge(arr,temp_arr,low,mid,high)
    return(res)


def merge(self,arr,temp_arr,low,mid,high):
   i=low
   j=mid+1
   k=low
   count=0
   while(i<=mid and j<=high):
       if(arr[i]<=arr[j]):
           # no inversion
           temp_arr[k]=arr[i]
           k+=1
           i+=1
       else:
           temp_arr[k]=arr[j]
           count+=(mid-i+1)
           k+=1
           j+=1
   while(i<=mid):
       temp_arr[k]=arr[i]
       k+=1
       i+=1
   while(j<=high):
       temp_arr[k]=arr[j]
       k+=1
       j+=1
   for i in range(low,high+1):
       arr[i]=temp_arr[i]
   return(count)

arr=[2,4,1,3,5]
n=len(arr)
bit=[2,4,1,3,5]
inversionCount(bit,arr,n)
print(bit)