import math
class Solution:
    #MEMOIZATION
    def numofcoins(self,coins,M,V,dp):
        if V==0:
            return 0
        if V<0:
            return math.inf
        if dp[V]!=-1:
            return dp[V]
        minc=math.inf
        for i in range(0,M):
            if V>=coins[i]:
                ans=self.numofcoins(coins,M,V-coins[i],dp)
                if ans!=math.inf:
                    minc=min(minc,1+ans)
        dp[V]=minc
        return dp[V]
    
    #TABULATION
    def numcoinsTab(self,coins,M,V):
        dp=[math.inf]*(V+1)
        dp[0]=0
        for i in range(1,V+1):
            for j in range(0,M):
                if (i-coins[j])>=0 and dp[i-coins[j]]!= math.inf:
                    dp[i]=min(dp[i],1+dp[i-coins[j]])
        
        if dp[V]==math.inf:
            return -1
        return dp[V]
        
    def minCoins(self, coins, M, V):
    # dp=[-1]*(V+1)
    # ans=self.numofcoins(coins,M,V,dp)
    # if ans==math.inf:
    #     return -1
    # return ans
        return self.numcoinsTab(coins,M,V)