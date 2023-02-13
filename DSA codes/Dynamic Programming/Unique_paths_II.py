class Solution:
    #MEMOIZATION

    def path(self,Grid,i,j,dp):
        if i==0 and j==0:
            return 1
        if (i<0 or j<0):
            return 0
        if Grid[i][j]==1:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.path(Grid,i-1,j,dp)
        left=self.path(Grid,i,j-1,dp)
        dp[i][j]=up+left
        return dp[i][j]
    
    #TABULATION

    def pathTab(self,Grid,m,n):
        dp=[[-1]*n for i in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                else:
                    up,left=0,0
                    if i>0 and Grid[i-1][j]!=1:
                        up=dp[i-1][j]
                    if j>0 and Grid[i][j-1]!=1:
                        left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]==1:
            return 0
        if obstacleGrid[0][0]==1:
            return 0
        # dp=[[-1 for i in range(n)] for j in range(m)]
        # return self.path(obstacleGrid,m-1,n-1,dp)
        return self.pathTab(obstacleGrid,m,n)