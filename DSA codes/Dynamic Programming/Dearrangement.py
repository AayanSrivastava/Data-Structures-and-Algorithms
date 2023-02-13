class Solution:
    #MEMOIZATION
    
    def memoization(self,N,dp):
        if N<=1:
            return 0
        if N==2:
            return 1
        if dp[N]!=-1:
            return dp[N]
            
        dp[N]=(N-1)%1000000007*(self.memoization(N-2,dp)%1000000007+self.memoization(N-1,dp)%1000000007)
        return dp[N]
    #TABULATION
    
    def solveTab(self,N):
        dp=[-1]*(N+1)
        dp[0],dp[1],dp[2]=0,0,1
        for i in range(3,N+1):
            dp[i]=(i-1)*(dp[i-1]+dp[i-2])%1000000007
            
        return dp[N]
        
    def disarrange(self, N):
        # dp=[-1]*(N+1)
        # return self.memoization(N,dp)
        return self.solveTab(N)