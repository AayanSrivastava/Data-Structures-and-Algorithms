class Solution:
    def solve(self,mat,i,j,maxi,dp):
        if i>=len(mat) or j >=len(mat[0]):
            return 0
        
        if dp[i][j]!=-1:
            return dp[i][j]
            
        right=self.solve(mat,i,j+1,maxi,dp)
        down=self.solve(mat,i+1,j,maxi,dp)
        diagonal=self.solve(mat,i+1,j+1,maxi,dp)
        
        if mat[i][j]=='1':
            dp[i][j]=1+min(right,down,diagonal)
            maxi=max(maxi,dp[i][j])
            return dp[i][j]
        else:
            dp[i][j]=0
            return dp[i][j]
        
    def solvetab(self,mat):
        n,m=len(mat),len(mat[0])
        dp=[[0]*(m+1)for i in range(n+1)]
        maxi=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if mat[i-1][j-1]==1:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                    maxi=max(maxi,dp[i][j])
        return maxi
            
    def solveopt(self,mat):
        n,m=len(mat),len(mat[0])
        next=[0]*(m+1)
        maxi=0
        for i in range(1,n+1):
            cur=[0]*(m+1)
            for j in range(1,m+1):
                if mat[i-1][j-1]==1:
                    cur[j]=1+min(next[j-1],next[j],cur[j-1])
                    maxi=max(maxi,cur[j])
            next=cur
        return maxi
            
    def maxSquare(self, n, m, mat):
        # maxi=0
        # dp=[[-1]*m for i in range(n)]
        # return self.solve(mat,0,0,maxi,dp)
        # return self.solvetab(mat)
        return self.solveopt(mat)