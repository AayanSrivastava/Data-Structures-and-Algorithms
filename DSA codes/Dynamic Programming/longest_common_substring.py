class Solution:
    
    def solvetab(self,s1,s2):
        dp=[[0]*(len(s2)+1) for j in range(len(s1)+1)]
        ans=0
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                    ans=max(dp[i][j],ans)
                else:
                    dp[i][j]=0
                
        return ans
        
    def solveopt(self,s1,s2):
        prev=[0]*(len(s2)+1)
        ans=0
        for i in range(1,len(s1)+1):
            cur=[0]*(len(s2)+1)
            for j in range(1,len(s2)+1):
                if s1[i-1]==s2[j-1]:
                    cur[j] = 1+ prev[j-1]
                    ans=max(cur[j],ans)
                else:
                    cur[j]=0
            prev=cur
        return ans
    
    def longestCommonSubstr(self, S1, S2, n, m):
        # return self.solvetab(S1,S2)
        return self.solveopt(S1,S2)

# Solved