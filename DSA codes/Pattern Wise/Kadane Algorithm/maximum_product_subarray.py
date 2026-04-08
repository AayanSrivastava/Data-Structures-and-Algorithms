class Solution:
    def maxProduct(self, nums) -> int:
        minending = maxending = res = nums[0]
        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = minending*nums[i]
            v3 = maxending*nums[i]

            minending = min(v1, min(v2, v3))
            maxending = max(v1, max(v2, v3))

            res = max(res, max(minending, maxending))
        
        return res