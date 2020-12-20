def rotateImage(matrix):
     
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            #Swap index values
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        matrix[i] = matrix[i][::-1]
    return matrix


a = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(rotateImage(a))

[[7, 8, 9],
 [4, 5, 6], 
 [1, 2, 3]]