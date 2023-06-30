class Solution:
    def solvememo(self,index,buy,prices,dp,k):
        if index==len(prices):
            return 0

        if k==0:
            return 0

        if dp[index][buy][k]!=-1:
            return dp[index][buy][k]

        profit=0
        if buy:
            buyit=-prices[index]+self.solvememo(index+1,0,prices,dp,k)
            skipit=0+self.solvememo(index+1,1,prices,dp,k)
            profit=max(buyit,skipit)
        else:
            sellit=+prices[index]+self.solvememo(index+1,1,prices,dp,k-1)
            skipit=0+self.solvememo(index+1,0,prices,dp,k)
            profit=max(sellit,skipit)
        dp[index][buy][k]=profit
        return dp[index][buy][k]
    
    def solvetab(self,prices,lim):
        n=len(prices)
        dp=[[[0]*(lim+1) for i in range(2)] for j in range(len(prices)+1)]
        for index in range(n-1,-1,-1):
            for buy in range(2):
                for k in range(1,lim+1):
                    profit=0
                    if buy:
                        buyit=-prices[index]+dp[index+1][0][k]
                        skipit=0+dp[index+1][1][k]
                        profit=max(buyit,skipit)
                    else:
                        sellit=+prices[index]+dp[index+1][1][k-1]
                        skipit=0+dp[index+1][0][k]
                        profit=max(sellit,skipit)
                    dp[index][buy][k]=profit
        return dp[0][1][k]
    
    def solveopt(self,prices,lim):
        n=len(prices)
        next=[[0]*(lim+1) for i in range(2)]
        cur=[[0]*(lim+1) for i in range(2)]
        for index in range(n-1,-1,-1):
            for buy in range(2):
                for k in range(1,lim+1):
                    profit=0
                    if buy:
                        buyit=-prices[index]+next[0][k]
                        skipit=0+next[1][k]
                        profit=max(buyit,skipit)
                    else:
                        sellit=+prices[index]+next[1][k-1]
                        skipit=0+next[0][k]
                        profit=max(sellit,skipit)
                    cur[buy][k]=profit
            next=cur
        return next[1][k]

    def maxProfit(self, k,prices):
        # dp=[[[-1]*(k+1) for j in range(2)] for i in range(len(prices))]
        # return self.solvememo(0,1,prices,dp,k)
        # return self.solvetab(prices,k)
        return self.solveopt(prices,k)