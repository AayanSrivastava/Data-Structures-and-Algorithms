class Solution:

    #MEMOIZATION
    def solvememo(self,matrix,i,j,dp):
        if j<0 or j>=len(matrix[0]):
            return 1e9
        if i==0:
            return matrix[0][j]

        if dp[i][j]!=-1:
            return dp[i][j]

        s=matrix[i][j]+self.solvememo(matrix,i-1,j,dp)
        ld=matrix[i][j]+self.solvememo(matrix,i-1,j-1,dp)
        rd=matrix[i][j]+self.solvememo(matrix,i-1,j+1,dp)
        dp[i][j]=min(s,ld,rd)
        return dp[i][j]
    
    #TABULATION
    def solveTab(self,matrix):
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for i in range(m)]
        for j in range(n):
            dp[0][j]=matrix[0][j]
        
        for i in range(1,m):
            for j in range(n):
                s=matrix[i][j]+dp[i-1][j]
                ld,rd=1e9,1e9
                if j-1>=0: ld=matrix[i][j]+dp[i-1][j-1]
                if j+1<n: rd=matrix[i][j]+dp[i-1][j+1]
                dp[i][j]=min(s,ld,rd)
        mini=1e9
        for j in range(n):
            mini=min(mini,dp[m-1][j])
        return mini
    
    #SPACE_OPTIMIZATION
    def solveOpt(self,matrix):
        m,n=len(matrix),len(matrix[0])
        prev=[0]*n
        for j in range(n):
            prev[j]=matrix[0][j]
        
        for i in range(1,m):
            cur=[0]*n
            for j in range(n):
                s=matrix[i][j]+prev[j]
                ld,rd=1e9,1e9
                if j-1>=0: ld=matrix[i][j]+prev[j-1]
                if j+1<n: rd=matrix[i][j]+prev[j+1]
                cur[j]=min(s,ld,rd)
            prev=cur
        mini=1e9
        for j in range(n):
            mini=min(mini,prev[j])
        return mini

    def minFallingPathSum(self, matrix):
        m,n=len(matrix),len(matrix[0])
        # dp=[[-1]*m for i in range(n)]
        # mini=1e9
        # for j in range(1,n):
        #     mini=min(mini,self.solveTab(matrix,m-1,j,m,n))
        # return mini
        # return self.solveTab(matrix)
        return self.solveOpt(matrix)