def makeZero(matrix, item):
    '''
    Make row and column set of a given index.
    '''
    rows = len(matrix)
    cols = len(matrix[0])
    for idx in range(rows):
        matrix[idx][item[1]] = 0
    for idx in range(rows):
        matrix[item[0]][idx] = 0
    return matrix

def zeroMatrix(matrix):
    '''
    Find all indices with value zero and run makeZero for them.
    '''
    zeroList = []
    for idx, ritem in enumerate(matrix):
        for jdx, citem in enumerate(ritem):
            if citem == 0:
                zeroList.append((idx, jdx))
    for item in zeroList:
        matrix = makeZero(matrix, item)
    return matrix

def printMatrix(matrix):
    '''
    Print in an aesthetically pleasing manner.
    '''
    for r in matrix:
        for i in r:
            print(i, end=" ")
        print("")

if __name__ == '__main__':
    arr = [[5,6,7,8],
        [0,1,2,3],
        [4,5,2,0],
        [9,9,8,1]
        ]
    printMatrix(zeroMatrix(arr))