def searchMatrix(matrix,target,n,m):
    for i in range(n):
        for j in range(m):
            if  matrix[i][j]==target:
                print("true")
    return               
                             
matrix=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,19]
       
]  
target=3               
m=len(matrix) 
n=len(matrix[0])
print(searchMatrix(matrix,target,m,n))