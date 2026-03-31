class Solution:
    def minOperations(self, nums, x: int) -> int:
        i = 0
        target = sum(nums)-x
        maxi = -1
        window_sum = 0
        for j in range(len(nums)):
            window_sum+=nums[j]
        
            while i<=j and window_sum>target:
                window_sum-=nums[i]
                i+=1
            
            if window_sum == target:
                maxi = max(maxi, j-i+1)
        
        return len(nums)-maxi if maxi!=-1 else -1