def transpose(matrix, rows, cols):
    '''
    Find transpose of a given matrix.
    '''
    for r in range(rows):
        for c in range(r, cols):
            t = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = t
    return matrix

def reverseCols(matrix, cols):
    '''
    Reverse the columns of the matrix.
    '''
    for i in range(cols): 
        j = 0
        k = cols-1
        while j < k: 
            t = arr[j][i] 
            arr[j][i] = arr[k][i] 
            arr[k][i] = t 
            j += 1
            k -= 1
    return matrix

def rotateMatrix(matrix, rows, cols):
    '''
    Rotate matrix by 90 degrees.
    '''
    matrix = transpose(matrix, rows, cols)
    matrix = reverseCols(matrix, cols)
    return matrix

def printMatrix(matrix):
    '''
    Print in an aesthetically pleasing manner.
    '''
    for r in matrix:
        for i in r:
            print(i, end=" ")
        print("")

arr = [[1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12], 
        [13, 14, 15, 16] 
    ]

printMatrix(rotateMatrix(arr, 4, 4))

