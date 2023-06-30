class Solution:
    def solvememo(self,index,buy,prices,dp,limit):
        if index==len(prices):
            return 0

        if limit==0:
            return 0

        if dp[index][buy][limit]!=-1:
            return dp[index][buy][limit]

        profit=0
        if buy:
            buyit=-prices[index]+self.solvememo(index+1,0,prices,dp,limit)
            skipit=0+self.solvememo(index+1,1,prices,dp,limit)
            profit=max(buyit,skipit)
        else:
            sellit=+prices[index]+self.solvememo(index+1,1,prices,dp,limit-1)
            skipit=0+self.solvememo(index+1,0,prices,dp,limit)
            profit=max(sellit,skipit)
        dp[index][buy][limit]=profit
        return dp[index][buy][limit]
    
    def solvetab(self,prices):
        n=len(prices)
        dp=[[[0]*3 for i in range(2)] for i in range(len(prices)+1)]
        for index in range(n-1,-1,-1):
            for buy in range(2):
                for limit in range(1,3):
                    profit=0
                    if buy:
                        buyit=-prices[index]+dp[index+1][0][limit]
                        skipit=0+dp[index+1][1][limit]
                        profit=max(buyit,skipit)
                    else:
                        sellit=+prices[index]+dp[index+1][1][limit-1]
                        skipit=0+dp[index+1][0][limit]
                        profit=max(sellit,skipit)
                    dp[index][buy][limit]=profit
        return dp[0][1][2]
    
    def solveopt(self,prices):
        n=len(prices)
        next=[[0]*3 for i in range(2)]
        cur=[[0]*3 for i in range(2)]
        for index in range(n-1,-1,-1):
            for buy in range(2):
                for limit in range(1,3):
                    profit=0
                    if buy:
                        buyit=-prices[index]+next[0][limit]
                        skipit=0+next[1][limit]
                        profit=max(buyit,skipit)
                    else:
                        sellit=+prices[index]+next[1][limit-1]
                        skipit=0+next[0][limit]
                        profit=max(sellit,skipit)
                    cur[buy][limit]=profit
            next=cur
        return next[1][2]


    def maxProfit(self, prices):
        # dp=[[[-1]*3 for i in range(2)] for i in range(len(prices))]
        # return self.solvememo(0,1,prices,dp,2)
        # return self.solvetab(prices)
        return self.solveopt(prices)