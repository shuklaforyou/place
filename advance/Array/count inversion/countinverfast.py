def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                #print(arr[i],arr[j])
                inv_count += 1
  
    return inv_count
  
# Driver Code
arr = [2, 4, 1, 3, 5]
n = len(arr)
print("Number of inversions are",
      getInvCount(arr, n))

#this is good alogrthim but not optimise
#Time Complexity: O(n^2),
#Space Complexity:O(1)