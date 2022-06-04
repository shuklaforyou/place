matrix=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,19]
       
] 
n=4
m=4
for i in range(n):
    for j in range(m):
        if  matrix[i][j]==3:
            print("true")

print(len(matrix))
print(len(matrix[0]))