import sys 
t=[[-1 for i in range(100)]for j in range(100)]

def mcm(a,i,j):
    if (i==j):
        return 0
    if t[i][j]!=-1:
        return t[i][j]

    t[i][j]=sys.maxsize

    for k in range(i,j):
        t[i][j]=min(t[i][j],mcm(a, i, k) + mcm(a, k + 1, j)+ a[i - 1] * a[k] * a[j])


    return t[i][j]

def mco(a,n):
    i=1
    j=n-1
    return mcm(a,i,j)

a=[40,20,30,10,30]
n=len(a)
print(mco(a,n))



# import sys
# t = [[-1 for i in range(100)] for j in range(100)]

# # Function for matrix chain multiplication 
# def mcm(a, i, j):
#     if(i == j):
#         return 0
    
#     if(t[i][j] != -1):
#         return t[i][j]
    
#     t[i][j] = sys.maxsize
    
#     for k in range(i,j):
#         t[i][j] = min(t[i][j],mcm(a, i, k) + mcm(a, k + 1, j)+ a[i - 1] * a[k] * a[j])
    
#     return t[i][j]

# def mco(a,n):
#     i = 1
#     j = n - 1    
#     return mcm(a, i, j)


# arr =[40,20,30,10,30]
# n = len(arr)
# print("Minimum number of multiplications is",mco(arr, n))