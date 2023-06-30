class Solution:
    def solvememo(self,index,buy,prices,fee,dp):
        if index==len(prices):
            return 0
        if dp[index][buy]!=-1:
            return dp[index][buy]

        profit=0
        if buy:
            buyit=-prices[index]+self.solvememo(index+1,0,prices,fee,dp)
            skipit=0+self.solvememo(index+1,1,prices,fee,dp)
            profit=max(buyit,skipit)
        else:
            sellit=+prices[index]-fee+self.solvememo(index+1,1,prices,fee,dp)
            skipit=0+self.solvememo(index+1,0,prices,fee,dp)
            profit=max(sellit,skipit)
        dp[index][buy]=profit
        return dp[index][buy]
    
    def solvetab(self,prices,fee):
        n=len(prices)
        dp=[[0]*2 for i in range(len(prices)+1)]
        for index in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy:
                    buyit=-prices[index]+dp[index+1][0]
                    skipit=0+dp[index+1][1]
                    profit=max(buyit,skipit)
                else:
                    sellit=+prices[index]-fee+dp[index+1][1]
                    skipit=0+dp[index+1][0]
                    profit=max(sellit,skipit)
                dp[index][buy]=profit
        return dp[0][1]
    
    def solveopt(self,prices,fee):
        n=len(prices)
        prev=[0]*2
        for index in range(n-1,-1,-1):
            cur=[0]*2
            for buy in range(2):
                profit=0
                if buy:
                    buyit=-prices[index]+prev[0]
                    skipit=0+prev[1]
                    profit=max(buyit,skipit)
                else:
                    sellit=+prices[index]-fee+prev[1]
                    skipit=0+prev[0]
                    profit=max(sellit,skipit)
                cur[buy]=profit
            prev=cur
        return prev[1]

    def maxProfit(self,prices,fee):
        # dp=[[-1]*2 for i in range(len(prices))]
        # return self.solvememo(0,1,prices,fee,dp)
        # return self.solvetab(prices,fee)
        return self.solveopt(prices,fee)