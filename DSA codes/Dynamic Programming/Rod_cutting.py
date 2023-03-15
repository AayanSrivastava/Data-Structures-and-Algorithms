class Solution:
    def solvememo(self,ind,price,n,dp):
        if ind==0:
            return n*price[0]
        
        if dp[ind][n]!=-1:
            return dp[ind][n]
        
        nottake=self.solvememo(ind-1,price,n,dp)
        take=0
        rodlength=ind+1
        if rodlength<=n:
            take=price[ind]+self.solvememo(ind,price,n-rodlength,dp)
        
        dp[ind][n]=max(take,nottake)
        return dp[ind][n]
    
    def solveTab(self,price,n):
        dp=[[0]*(n+1) for i in range(n)]
        for j in range(n+1):
            dp[0][j]=j*price[0]
        for i in range(1,n):
            for j in range(n+1):
                nottake=dp[i-1][j]
                take=0
                rodlength=i+1
                if rodlength<=j:
                    take=price[i]+dp[i][j-rodlength]
                dp[i][j]=max(take,nottake)
        return dp[n-1][n]
    
    def solveOptim(self,price,n):
        prev=[0]*(n+1)
        cur=[0]*(n+1)
        for j in range(n+1):
            prev[j]=j*price[0]
        for i in range(1,n):
            for j in range(n+1):
                nottake=prev[j]
                take=0
                rodlength=i+1
                if rodlength<=j:
                    take=price[i]+cur[j-rodlength]
                cur[j]=max(take,nottake)
            prev=cur
        return prev[n]
    
    def solvemoreOptim(self,price,n):
        prev=[0]*(n+1)
        for j in range(n+1):
            prev[j]=j*price[0]
        for i in range(1,n):
            for j in range(n+1):
                nottake=prev[j]
                take=0
                rodlength=i+1
                if rodlength<=j:
                    take=price[i]+prev[j-rodlength]
                prev[j]=max(take,nottake)
        return prev[n]
        
    def cutRod(self, price, n):
        # dp=[[-1]*(n+1) for i in range(n)]
        # return self.solvememo(n-1,price,n,dp)
        # return self.solveTab(price,n)
        # return self.solveOptim(price,n)
        return self.solvemoreOptim(price,n)