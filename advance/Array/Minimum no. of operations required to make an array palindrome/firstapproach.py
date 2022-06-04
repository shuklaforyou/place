def PalinArray(arr ,n):
   if all(str(i)==str(i)[::-1] for i in arr):
       return 1
   else:
       return 0


n=int(input("number of test case :-"))
for i in range(n):
    arr_size=int(input())
    arr=list(map(int,input().split()))
    print(PalinArray(arr,arr_size))