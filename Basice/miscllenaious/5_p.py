def getsingle(arr,n):
    ones=0
    twos=0
    for i in range(n):
        twos=twos^(ones&arr[i])
        ones=ones^arr[i]
        print(ones,twos)
        commen_bits =~(ones & twos )
        print(commen_bits,"y")
        ones &= commen_bits
        twos &= commen_bits
        print(ones,twos)
    return ones

arr=[3,3,2,3]
n=len(arr)
print("the element with single ocurrance is ", getsingle(arr,n))
