class Solution:
    def waysToMakeFair(self, nums) -> int:
        even_total = sum(nums[i] for i in range(0, len(nums), 2))
        odd_total  = sum(nums[i] for i in range(1, len(nums), 2))
        
        left_even = left_odd = 0
        count = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                even_total -= nums[i]
            else:
                odd_total -= nums[i]
            
            if left_even + odd_total == left_odd + even_total:
                count += 1
            
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]
        
        return count