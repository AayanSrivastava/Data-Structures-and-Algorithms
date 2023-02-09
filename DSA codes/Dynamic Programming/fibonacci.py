class Solution:
    #MEMOIZATION

    def fibo(self,n,dp):
        if n<=1:
            return n
        if dp[n]!=-1:
            return dp[n]
            
        dp[n]=self.fibo(n-1,dp)+self.fibo(n-2,dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.fibo(n,dp)
    
    #TABULATION

    def fib1(self, n: int) -> int:
        if n<=1:
            return n
        dp=[-1]*(n+1)
        dp[0],dp[1]=0,1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

    #OPTIMIZATION

    def fib2(self, n: int) -> int:
        if n<=1:
            return n
        prev1,prev=0,1
        for i in range(2,n+1):
            cur=prev+prev1
            prev1=prev
            prev=cur
        return cur