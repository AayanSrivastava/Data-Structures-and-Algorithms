class Solution:
    def solvememo(self,s1,s2,i,j,dp):
        if j<0:
            return 1
        if i<0:
            return 0
        
        if dp[i][j]!=-1:
            return dp[i][j]

        if s1[i]==s2[j]:
            dp[i][j]=self.solvememo(s1,s2,i-1,j-1,dp)+self.solvememo(s1,s2,i-1,j,dp)
        else:
            dp[i][j]=self.solvememo(s1,s2,i-1,j,dp)

        return dp[i][j]

    def solvetab(self,s1,s2):
        n,m=len(s1),len(s2)
        dp=[[0]*(m+1) for i in range(n+1)]
        
        for i in range(n):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][m]

    def solveopt(self,s1,s2):
        n,m=len(s1),len(s2)
        prev=[0]*(m+1)
        prev[0]=1
        for i in range(1,n+1):
            cur=[0]*(m+1)
            cur[0]=1
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    cur[j]=prev[j-1]+prev[j]
                else:
                    cur[j]=prev[j]
            prev=cur

        return prev[m]
    
    #1D Array Optimization
    def solveopt1D(self,s1,s2):
        n,m=len(s1),len(s2)
        dp=[0]*(m+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(m,0,-1):
                if s1[i-1]==s2[j-1]:
                    dp[j]=dp[j-1]+dp[j]

        return dp[m]


    def numDistinct(self,s,t):
        # n,m=len(s),len(t)
        # dp=[[-1]*m for i in range(n)]
        # return self.solvememo(s,t,n-1,m-1,dp)
        # return self.solvetab(s,t)
        return self.solveopt(s,t)