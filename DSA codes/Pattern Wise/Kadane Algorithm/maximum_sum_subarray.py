class Solution:
    def maxSubArray(self, nums) -> int:
        bestending = res = nums[0]
        for i in range(1,len(nums)):
            v1 = bestending + nums[i]
            v2 = nums[i]
            bestending = max(v1, v2)
            res = max(res, bestending)
        
        return res