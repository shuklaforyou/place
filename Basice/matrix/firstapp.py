

# arr1=([
#            [1,2,3],
#            [4,5,6]
# ])

# print(arr1[0][0])


row = int(input("enter row "))
col = int(input("enter col"))

print("enter the element for matrix")

matrix1= [[int(input()) for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()

print(matrix1.len)

# print("enter the element for matrix 2")

# matrix2= [[int(input()) for i in range(col)] for j in range(row)]
# for i in range(row):
#     for j in range(col):
#         print(matrix2[i][j],end=" ")
#     print()