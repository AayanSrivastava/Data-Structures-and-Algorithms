import math
class Solution:
    #MEMOIZATION
    
    def min1(self,height,n,dp):
        if n==0:
            return 0
            
        if dp[n]!=-1:
            return dp[n]
        left=math.inf  
        left=self.min1(height,n-1,dp)+abs(height[n]-height[n-1])
        right=math.inf
        if n>1:
            right=self.min1(height,n-2,dp)+abs(height[n]-height[n-2])
        dp[n]=min(left,right)
        return dp[n]
        
    def minimumEnergy(self, height, n):
        dp=[-1]*(n)
        self.min1(height,n-1,dp)
        return dp[n-1]
        
        #TABULATION
        
        # dp=[-1]*(n+1)
        # dp[0],dp[1]=0,0
        # for i in range(1,n):
        #     left=dp[i-1]+abs(height[i]-height[i-1])
        #     right=math.inf
        #     if i>1:
        #         right=dp[i-2]+abs(height[i]-height[i-2])
        #     dp[i]=min(left,right)
        # return dp[n-1]
        
        #SPACE OPTIMIZATION
        
        # prev,prev2=0,0
        # for i in range(1,n):
        #     l1=prev+abs(height[i]-height[i-1])
        #     l2=math.inf
        #     if i>1:
        #         l2=prev2+abs(height[i]-height[i-2])
        #     cur=min(l1,l2)
        #     prev2=prev
        #     prev=cur
        # return prev