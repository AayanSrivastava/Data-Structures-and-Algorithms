class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        total = sum(nums)
        globalmax = globalmin = maxsum = minsum = res = nums[0]
        for i in range(1,len(nums)):
            maxsum = max(nums[i], maxsum + nums[i])
            minsum = min(nums[i], minsum + nums[i])

            globalmax = max(globalmax, maxsum)
            globalmin = min(globalmin, minsum)

        if globalmax < 0:
            return globalmax

        return max(globalmax, total-globalmin)