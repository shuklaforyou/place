# Python3 program to implement
# the above approach

# Function returns the required count



def PermuteTheArray(A, n):

	arr = [0] * n

	# Store the indices of the
	# elements present in A[].
	for i in range(n):
		arr[A[i] - 1] = i

	# Store the maximum and
	# minimum index of the
	# elements from 1 to i.
	mini = n
	maxi = 0
	count = 0
	for i in range(n):

		# Update maxi and mini, to
		# store minimum and maximum
		# index for permutation
		# of elements from 1 to i+1
		mini = min(mini, arr[i])
		maxi = max(maxi, arr[i])

		# If difference between maxi
		# and mini is equal to i
		if (maxi - mini == i):

			# Increase count
			count += 1
    
	# Return final count
	return count,print(arr)

# Driver Code


A= [ 2,3,1 ]
	
print(PermuteTheArray(A, 3))

# This code is contributed by chitranayal
