class Solution:
    def solve(self,s1,s2,i,j,dp):
        if i<0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]

        if s1[i]==s2[j] and i!=j:
            dp[i][j]= 1+ self.solve(s1,s2,i-1,j-1,dp)
        else:
            dp[i][j]=max(self.solve(s1,s2,i-1,j,dp),self.solve(s1,s2,i,j-1,dp))
        
        return dp[i][j]
    
    def solvetab(self,s1,s2):
        dp=[[0]*(len(s2)+1) for j in range(len(s1)+1)]
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                ans=0
                if s1[i]==s2[j] and i!=j:
                    ans = 1+ dp[i+1][j+1]
                else:
                    ans=max(dp[i+1][j],dp[i][j+1])
                
                dp[i][j]=ans
        return dp[0][0]

    def solveopt(self,s1,s2):
        prev=[0]*(len(s2)+1)
        for i in range(len(s1)-1,-1,-1):
            cur=[0]*(len(s2)+1)
            for j in range(len(s2)-1,-1,-1):
                ans=0
                if s1[i]==s2[j] and i!=j:
                    ans = 1+ prev[j+1]
                else:
                    ans=max(prev[j],cur[j+1])
                cur[j]=ans
            prev=cur
        return prev[0]

    def LongestRepeatingSubsequence(self, str):
        n=len(str)
        dp=[[-1]*n for j in range(n)]
        return self.solve(str,str,n-1,n-1,dp)
        # return self.solvetab(str,str)
        # return self.solveopt(str,str)