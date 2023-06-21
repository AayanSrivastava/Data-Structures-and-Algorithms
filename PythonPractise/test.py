def rotate(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j]=matrix[j][i]
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotate(matrix))
print()
print(rotate(matrix))