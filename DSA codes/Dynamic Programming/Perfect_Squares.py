import math
class Solution:
    def solve(self,n,dp):
        if n==0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        
        ans=n
        for i in range(1,int(math.sqrt(n))+1):
            temp=i*i
            ans=min(ans,1+self.solve(n-temp,dp))
        
        dp[n]=ans
        return dp[n]
    
    def solveTab(self,n):
        dp=[math.inf]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for j in range(1,int(math.sqrt(n))+1):
                temp=j*j
                if i-temp>=0:
                    dp[i]=min(dp[i],1+dp[i-temp])
        
        return dp[n]

    def numSquares(self, n: int) -> int:
        # dp=[-1]*(n+1)
        # return self.solve(n,dp)
        return self.solveTab(n)