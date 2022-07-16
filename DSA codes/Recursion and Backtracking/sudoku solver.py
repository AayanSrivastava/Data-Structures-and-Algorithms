class Solution:
    def solve(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    for c in range(1,10):
                        if self.isvalid(board,i,j,str(c)):
                            board[i][j]=str(c)
                            
                            if self.solve(board) == True:
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True
    
    def isvalid(self,board,row,col,c):
        for i in range(0,9):
            if board[i][col] == c:
                return False
            
            if board[row][i] == c:
                return False
            
            if (board[3 * (row//3) + i//3][3 * (col//3) + i%3] == c):
                return False

        return True
    
    def solveSudoku(self, board):
        self.solve(board)
        return board
        
l=Solution()
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(l.solveSudoku(board))