class Solution:
    # def addsol(self,ans,board,n):
    #     temp=[]
    #     for i in range(n):
    #         for j in range(n):
    #             temp.append(board[i][j])
    #     ans.append(temp)
    
    def issafe(self,row,col,board,n):
        x=row
        y=col
        # check for same row
        while y>=0:
            if board[x][y]==1:
                return False
            y-=1

        x=row
        y=col
        # check for diagonal
        while x>=0 and y>=0:
            if board[x][y]==1:
                return False
            x-=1
            y-=1
        
        x=row
        y=col
        # check for diagonal
        while x<n and y>=0:
            if board[x][y]==1:
                return False
            y-=1
            x+=1

        return True

    def solve(self,col,ans,board,n):
        # base_case
        if col==n:
            ans.append(board)
            return
        # solve 1 case and rest recursion will take care
        
        for row in range(n):
            if self.issafe(row,col,board,n):
                board[row][col]=1
                self.solve(col+1,ans,board,n)
                # backtrack
                board[row][col]=0

    def Nqueen(self,n):
        board=[[0]*n for i in range(n)]
        ans=[]
        self.solve(0,ans,board,n) 
        return ans
    
l=Solution()
n=4
print(l.Nqueen(n))