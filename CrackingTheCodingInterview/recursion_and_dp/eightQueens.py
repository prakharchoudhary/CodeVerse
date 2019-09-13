k = 1 
'''
Prints the board.
'''
def printSolution(board):  
    global k 
    print(k, "-\n") 
    k = k + 1
    for i in range(8):  
        for j in range(8): 
            print(board[i][j], end = " ") 
        print("\n") 
    print("\n")  

'''
Steps to check if currently chosen block is safe:
- Check the row towards the left for a queen.
- Check the left halves of the diagonals.
'''
def isSafe(board, row, col) : 
    # Check this row on left side  
    for i in range(col):  
        if (board[row][i]):  
            return False
  
    # Check upper diagonal on left side  
    i = row 
    j = col 
    while i >= 0 and j >= 0: 
        if(board[i][j]): 
            return False 
        i -= 1
        j -= 1
  
    # Check lower diagonal on left side  
    i = row 
    j = col 
    while j >= 0 and i < 8: 
        if(board[i][j]): 
            return False
        i = i + 1
        j = j - 1
  
    return True
  
def eightQueenUtil(board, col) : 
    if (col == 8):  
        printSolution(board)  
        return True

    res = False

    for i in range(8): 
        ''' Check if queen can be placed on  
        board[i][col] '''
        if (isSafe(board, i, col)):  
            # Place this queen in board[i][col]  
            board[i][col] = 1  
            # Make result true if any placement  
            # is possible  
            res = eightQueenUtil(board, col + 1) or res  
            board[i][col] = 0 # BACKTRACK  

    return res 

def eightQueen() : 
    board = [[0 for j in range(8)]  
                for i in range(8)]
 
    if (eightQueenUtil(board, 0) == False):  
        print("Solution does not exist")  
        return

    return

if __name__ == '__main__':  
    eightQueen()