class Solution:
    def exist(self, board, word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if self.dfs(board, word, i, j, 0):
                        return True
        return False

    def dfs(self, board, word, r, c, index):
        rows = len(board)
        cols = len(board[0])

        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >=cols:
            return False
        if board[r][c]!=word[index]:
            return False
        
        temp = board[r][c]
        board[r][c] = "#"

        res = (self.dfs(board, word, r+1, c, index+1) or self.dfs(board, word, r-1, c, index+1) or self.dfs(board, word, r, c+1, index+1) or self.dfs(board, word, r, c-1, index+1))

        board[r][c] = temp
        return res

if __name__ == "__main__":
    obj = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(obj.exist(board, word))