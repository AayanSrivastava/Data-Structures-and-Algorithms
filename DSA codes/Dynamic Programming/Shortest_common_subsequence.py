class Solution:
    def solvememo(self,X,Y,i,j,dp):
        if i<0 or j<0:
            return 0
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if X[i]==Y[j]:
            dp[i][j]=1+self.solvememo(X,Y,i-1,j-1,dp)
        else:
            dp[i][j]=max(self.solvememo(X,Y,i-1,j,dp),self.solvememo(X,Y,i,j-1,dp))
        
        return dp[i][j]
        
    def solvetab(self,X,Y,m,n):
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if X[i-1]==Y[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
        return dp[-1][-1]
        
    def solveopt(self,X,Y,m,n):
        prev=[0]*(n+1)
        for i in range(1,m+1):
            cur=[0]*(n+1)
            for j in range(1,n+1):
                if X[i-1]==Y[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(prev[j],cur[j-1])
            
            prev=cur
            
        return cur[-1]
    
    #Function to find length of shortest common supersequence of two strings
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp=[[-1]*(n) for i in range(m)]
        return m+n-self.solvememo(X,Y,m-1,n-1,dp)
        # return m+n-self.solvetab(X,Y,m,n)
        # return m+n-self.solveopt(X,Y,m,n)