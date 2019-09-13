def fillColor(grid, i, j, c, r = None):
    '''
    grid : matrix of pixels.
    i : row number of the target pixel or y-coordinate.
    j : column number of the target pixel or x-coordinate.
    c : color to fill in.
    r:  color to be replaced
    '''
    i_possible = i >= 0 and i < len(grid)
    j_possible = j >= 0 and j < len(grid[0])
    
    if not (i_possible and j_possible):
        return grid

    if not r:
        # In the beginning, the color to be replaced is selected.
        r = grid[i][j]
    else:
        # if anyother color than then one to be replaced is encountered,
        # do nothing.
        if r != grid[i][j]:
            return grid
    grid[i][j] = c

    fillColor(grid, i-1, j-1, c, r=r)
    fillColor(grid, i-1, j, c, r=r)
    fillColor(grid, i-1, j+1, c, r=r)
    fillColor(grid, i, j-1, c, r=r)
    fillColor(grid, i, j+1, c, r=r)
    fillColor(grid, i+1, j-1, c, r=r)
    fillColor(grid, i+1, j, c, r=r)
    fillColor(grid, i+1, j+1, c, r=r)
    return grid

def printGrid(matrix):
    for row in matrix:
        print(' '.join(list(map(str, row))))

if __name__ == '__main__':
    grid = [[1,1,1,1,1],
            [0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,1,1,1,0],
            [1,1,1,1,1]
        ]
    printGrid(fillColor(grid, 2, 2, -1))