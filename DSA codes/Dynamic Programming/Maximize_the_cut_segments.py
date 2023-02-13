class Solution:
    #MEMOIZATION

    def cuts(self,n,x,y,z,dp):
        if n==0:
            return 0
        if n<0:
            return float('-inf')
            
        if dp[n]!=-1:
            return dp[n]
        a=self.cuts(n-x,x,y,z,dp)+1
        b=self.cuts(n-y,x,y,z,dp)+1
        c=self.cuts(n-z,x,y,z,dp)+1
        dp[n]=max(a,max(b,c))
        return dp[n]
    
    #TABULATION

    def cutsTab(self,n,x,y,z):
        dp=[float('-inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            if i>=x:
                dp[i]=max(dp[i],dp[i-x]+1)
            if i>=y:
                dp[i]=max(dp[i],dp[i-y]+1)
            if i>=z:
                dp[i]=max(dp[i],dp[i-z]+1)
        if dp[n]<0:
            return 0
        return dp[n]
        
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        # dp=[-1]*(n+1)
        # ans=self.cuts(n,x,y,z,dp)
        # if ans<0:
        #     return 0
        # else:
        #     return ans
        return self.cutsTab(n,x,y,z)