class Solution:
    def solvememo(self,s,p,i,j,dp):
        #base case
        if i<0 and j<0:
            return True
        if i>=0 and j<0:
            return False
        if i<0 and j>=0:
            for k in range(j+1):
                if p[k]!='*':
                    return False
            return True
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if s[i]==p[j] or p[j]=='?':
            dp[i][j]=self.solvememo(s,p,i-1,j-1,dp)
        elif p[j]=='*':
            dp[i][j]=self.solvememo(s,p,i-1,j,dp) or self.solvememo(s,p,i,j-1,dp)
        else:
            return False
        return dp[i][j]
    
    def solvetab(self,s,p):
        n,m=len(s),len(p)
        dp=[[0]*(m+1) for i in range(n+1)]
        dp[0][0]=1
        for j in range(1,m+1):
            flag=True
            for k in range(1,j+1):
                if p[k-1]!='*':
                    flag=False
                    break
            dp[0][j]=flag
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
        return dp[n][m]
    
    def solveopt(self,s,p):
        n,m=len(s),len(p)
        prev=[0]*(m+1)
        prev[0]=1
        for j in range(1,m+1):
            flag=True
            for k in range(1,j+1):
                if p[k-1]!='*':
                    flag=False
                    break
            prev[j]=flag
        
        for i in range(1,n+1):
            cur=[0]*(m+1)
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    cur[j]=prev[j-1]
                elif p[j-1]=='*':
                    cur[j]=prev[j] or cur[j-1]
                else:
                    cur[j]=False
            prev=cur
        return prev[m]


    def isMatch(self,s,p):
        # n,m=len(s),len(p)
        # dp=[[-1]*m for i in range(n)]
        # return self.solvememo(s,p,n-1,m-1,dp)
        # return self.solvetab(s,p)
        return self.solveopt(s,p)