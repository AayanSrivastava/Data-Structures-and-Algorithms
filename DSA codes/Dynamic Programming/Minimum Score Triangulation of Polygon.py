class Solution:
    def solve(self,values,i,j,dp):
        if i+1==j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]

        ans=1e9
        for k in range(i+1,j):
            ans=min(ans,values[i]*values[j]*values[k] + self.solve(values,i,k,dp)+self.solve(values,k,j,dp))
            dp[i][j]=ans
        return dp[i][j]
    
    def solvetab(self,values,n):
        dp=[[0]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                ans=1e9
                for k in range(i+1,j):
                    ans=min(ans,values[i]*values[j]*values[k] + dp[i][k]+dp[k][j])
                dp[i][j]=ans
        return dp[0][n-1]

    def minScoreTriangulation(self, values):
        n=len(values)
        # dp=[[-1]*n for i in range(n)]
        # return self.solve(values,0,n-1,dp)
        return self.solvetab(values,n)