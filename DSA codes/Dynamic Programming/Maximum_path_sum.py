class Solution:

    #MEMOIZATION
    def solvememo(self,matrix,i,j,dp):
        if j<0 or j>=len(matrix[0]):
            return -1e9
        if i==0:
            return matrix[0][j]
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        s=matrix[i][j]+self.solvememo(matrix,i-1,j,dp)
        ld=matrix[i][j]+self.solvememo(matrix,i-1,j-1,dp)
        rd=matrix[i][j]+self.solvememo(matrix,i-1,j+1,dp)
        dp[i][j]=max(s,ld,rd)
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
                ld,rd=-1e9,-1e9
                if j-1>=0: ld=matrix[i][j]+dp[i-1][j-1]
                if j+1<n: rd=matrix[i][j]+dp[i-1][j+1]
                dp[i][j]=max(s,ld,rd)
        maxi=-1e9
        for j in range(n):
            maxi=max(maxi,dp[m-1][j])
        return maxi
    
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
                ld,rd=-1e9,-1e9
                if j-1>=0: ld=matrix[i][j]+prev[j-1]
                if j+1<n: rd=matrix[i][j]+prev[j+1]
                cur[j]=max(s,ld,rd)
            prev=cur
        maxi=-1e9
        for j in range(n):
            maxi=max(maxi,prev[j])
        return maxi
        
    def maximumPath(self, N, Matrix):
        m,n=len(Matrix),len(Matrix[0])
        # dp=[[-1]*m for i in range(n)]
        # maxi=-1e9
        # for j in range(n):
        #     maxi=max(maxi,self.solvememo(Matrix,m-1,j,dp))
        # return maxi
        # return self.solveTab(Matrix)
        return self.solveOpt(Matrix)