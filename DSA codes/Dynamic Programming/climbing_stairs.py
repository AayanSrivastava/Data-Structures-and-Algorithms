class Solution:
    #MEMOIZATION

    def fib(self,n,dp):
        if n<=2:
            return n
        if dp[n]!=-1:
            return dp[n]
            
        dp[n]=self.fib(n-1,dp)+self.fib(n-2,dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        ans=self.fib(n,dp)
        return ans
    
    #TABULATION
    def fib1(self,n,dp):
        dp[0],dp[1],dp[2]=0,1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    
    #OPTIMIZATION

    def fib2(self,n,dp):
        if n<=2:
            return n
        a,b,c=0,1,2
        for i in range(3,n+1):
            d=b+c
            b=c
            c=d
        return d
        
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp=[-1]*(n+1)
        ans=self.fib1(n,dp)
        return ans
    
