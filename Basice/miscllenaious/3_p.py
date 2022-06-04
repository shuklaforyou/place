import sys
 
def findUnique(a, n, k):
     
    INT_SIZE = 8 * sys.getsizeof(int)
    count = [0] * INT_SIZE
     
    
    for i in range(INT_SIZE):
        for j in range(n):
            if ((a[j] & (1 << i)) != 0):
                count[i] += 1
 
    
    res = 0
    for i in range(INT_SIZE):
        res += (count[i] % k) * (1 << i)
    return res
 
# Driver Code
if __name__ == '__main__':
    a = [6, 2, 5, 2, 2, 6, 6]
    n = len(a)
    k = 3
    print(findUnique(a, n, k));

#Unique element in an array where all elements occur k times except one
