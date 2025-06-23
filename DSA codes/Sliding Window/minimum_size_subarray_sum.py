class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        i = 0
        window_sum = 0
        mini = float('inf')
        for j in range(len(nums)):
            window_sum+=nums[j]

            while window_sum>=target:
                mini = min(mini, j-i+1)
                window_sum-=nums[i]
                i+=1
        
        return mini if mini!= float('inf') else 0