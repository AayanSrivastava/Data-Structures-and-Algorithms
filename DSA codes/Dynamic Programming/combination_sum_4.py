class Solution:
    def solvememo(self,tar,nums,dp):
        if tar<0:
            return 0
        if tar==0:
            return 1
        if dp[tar]!=-1:
            return dp[tar]

        ans=0
        for i in range(len(nums)):
            ans+=self.solve(tar-nums[i],nums,dp)
        
        dp[tar]=ans
        return dp[tar]
    
    def solveTab(self,tar,nums):
        dp=[0]*(tar+1)
        dp[0]=1
        for i in range(1,tar+1):
            for j in range(len(nums)):
                if i-nums[j]>=0:
                    dp[i]+=dp[i-nums[j]]
        return dp[tar]

    def combinationSum4(self, nums, target):
        # dp=[-1]*(target+1)
        # return self.solvememo(target,nums,dp)
        return self.solveTab(target,nums)