class Solution:
    #MEMOIZATION

    def path(self,i,j,dp):
        if i==0 and j==0:
            return 1
        if (i<0 or j<0):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.path(i-1,j,dp)
        left=self.path(i,j-1,dp)
        dp[i][j]=up+left
        return dp[i][j]
    
    #TABULATION
    
    def pathTab(self,m,n):
        dp=[[-1]*n for i in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                else:
                    up,left=0,0
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[m-1][n-1]
        
    def NumberOfPaths(self,a, b):
        # dp=[[-1]*b for i in range(a)]
        # return self.path(a-1,b-1,dp)
        return self.pathTab(a,b)