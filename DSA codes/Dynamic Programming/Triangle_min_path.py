class Solution:
    
    #MEMOIZATION
    def solvememo(self,triangle,i,j,n,dp):
        if i==n-1:
            return triangle[i][j]
        
        if dp[i][j]!=-1:
            return dp[i][j]

        down=triangle[i][j]+self.solvememo(triangle,i+1,j,n,dp)
        diagonal=triangle[i][j]+self.solvememo(triangle,i+1,j+1,n,dp)
        dp[i][j]=min(down,diagonal)
        return dp[i][j]
    
    #TABULATION
    def solveTab(self,triangle,i,j,n):
        dp=[[0]*n for i in range(n)]
        for j in range(n):
            dp[n-1][j]=triangle[n-1][j]

        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down=triangle[i][j]+dp[i+1][j]
                diagonal=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down,diagonal)
        return dp[0][0]
        
    #SPACE_OPTIMIZATION
    def solveOpt(self,triangle,i,j,n):
        front=[0]*n
        for j in range(n):
            front[j]=triangle[n-1][j]

        for i in range(n-2,-1,-1):
            cur=[0]*n
            for j in range(i,-1,-1):
                down=triangle[i][j]+front[j]
                diagonal=triangle[i][j]+front[j+1]
                cur[j]=min(down,diagonal)
            front=cur
        return front[0]

    def minimumTotal(self, triangle):
        n=len(triangle)
        # dp=[[-1]*n for i in range(n)]
        # return self.solvememo(triangle,0,0,n,dp)
        # return self.solveTab(triangle,0,0,n)
        return self.solveOpt(triangle,0,0,n)