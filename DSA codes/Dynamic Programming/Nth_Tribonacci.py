class Solution:
    def fib(self,n,dp):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.fib(n-1,dp)+self.fib(n-2,dp)+self.fib(n-3,dp)
        return dp[n]

    def tribonacci(self, n):
        if n<=1:
            return n
        if n==2:
            return 1
        dp=[-1]*(n+1)
        self.fib(n,dp)
        return dp[n]