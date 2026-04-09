class Solution:
    def maxAbsoluteSum(self, nums) -> int:
        maxsum = minsum = res = 0
        for i in range(len(nums)):
            maxsum = max(nums[i], maxsum + nums[i])
            minsum = min(nums[i], minsum + nums[i])

            res = max(res, maxsum, abs(minsum))

        return res 