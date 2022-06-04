def smallestsubsumarray(arr,n,x):
    curr_sum=0
    min_len = n+1 
    min_sun=set()
    start=0
    end=0
    while (end<n):
        while(curr_sum<=x and end<n ):
            curr_sum +=arr[end]
            end +=1

        while(curr_sum >x and start <n):
            if (end-start<min_len):
                min_len=end-start
                #min_sun=arr[min_len]
            curr_sum-=arr[start]
            start+=1

    return min_len

arr=[1,4,45,6,0,19]
x=51
n=len(arr)

print(smallestsubsumarray(arr,n,x))