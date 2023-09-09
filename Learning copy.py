matrix = [[9,5,3],[0,7,-1],[-5,2,9]]
newmatrix = [[9,5,3],[0,7,-1],[-5,2,9]]
for i in range (len(matrix)):
    for j in range (len(matrix)):
        newmatrix[i][j] = (matrix[i-1][j] + matrix[i+1-len(matrix)][j] + matrix[i][j-1] + matrix[i][j+1-len(matrix)])
print(*newmatrix)