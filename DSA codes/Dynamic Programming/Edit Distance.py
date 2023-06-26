# deleted= solve(s,t,i-1,j,dp)
# insert= solve(s,t,i,j-1,dp)
# replace= solve(s,t,i-1,j-1,dp)

# similar to min operation to convert string A to string B

class Solution:
    def solvememo(self,s1,s2,i,j,dp):
        if i<0:
            return j+1
        if j<0:
            return i+1
        
        if dp[i][j]!=-1:
            return dp[i][j]

        if s1[i]==s2[j]:
            dp[i][j]=self.solvememo(s1,s2,i-1,j-1,dp)
        else:
            dp[i][j]=1+min(self.solvememo(s1,s2,i-1,j-1,dp),
                        self.solvememo(s1,s2,i-1,j,dp),
                        self.solvememo(s1,s2,i,j-1,dp))
        return dp[i][j]
    
    def solvetab(self,s1,s2):
        n,m=len(s1),len(s2)
        dp=[[-1]*(m+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0]=i
        for j in range(m+1):
            dp[0][j]=j
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    
        return dp[n][m]
    
    def solveopt(self,s1,s2):
        n,m=len(s1),len(s2)
        prev=[0]*(m+1)
        for j in range(m+1):
            prev[j]=j
        for i in range(1,n+1):
            cur=[0]*(m+1)
            cur[0]=i
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    cur[j]=prev[j-1]
                else:
                    cur[j]=1+min(prev[j],cur[j-1],prev[j-1])
            prev=cur
            
        return prev[m]
    
    def editDistance(self, s, t):
        # n,m=len(s),len(t)
        # dp=[[-1]*m for i in range(n)]
        # return self.solvememo(s,t,n-1,m-1,dp)
        # return self.solvetab(s,t)
        return self.solveopt(s,t)