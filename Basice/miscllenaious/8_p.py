def fun(n):
    return n & (n-1)

n=7
print('The number after unsetting the rightmost set bit',fun(n))
