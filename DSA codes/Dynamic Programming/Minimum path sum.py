class Solution:
    #MEMOIZATION
    def path(self,grid,i,j,dp):
        if i==0 and j==0:
            return grid[0][0]
        if (i<0 or j<0):
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.path(grid,i-1,j,dp)+grid[i][j]
        left=self.path(grid,i,j-1,dp)+grid[i][j]
        dp[i][j]=min(up,left)
        return dp[i][j]

    #TABULATION
    def pathTab(self,grid,m,n):
        dp=[[-1]*n for i in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    up,left=1e9,1e9
                    if i>0:
                        up=dp[i-1][j]+grid[i][j]
                    if j>0:
                        left=dp[i][j-1]+grid[i][j]
                    dp[i][j]=min(up,left)
        return dp[m-1][n-1]
    
    #OPTIMIZATION
    def pathOpt(self,grid,m,n):
        prev=[0]*n
        for i in range(m):
            cur=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    cur[j]=grid[i][j]
                else:
                    up,left=1e9,1e9
                    if i>0:
                        up=prev[j]+grid[i][j]
                    if j>0:
                        left=cur[j-1]+grid[i][j]
                    cur[j]=min(up,left)
            prev=cur
        return prev[n-1]
    
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        # dp=[[-1]*n for i in range(m)]
        # return self.path(grid,m-1,n-1,dp)
        # return self.pathTab(grid,m,n)
        return self.pathOpt(grid,m,n)