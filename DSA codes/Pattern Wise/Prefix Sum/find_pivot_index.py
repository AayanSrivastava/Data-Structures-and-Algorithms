class Solution:
    def pivotIndex(self, nums) -> int:
        prefix = {0:0}
        suffix = {len(nums)-1:0}
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] + nums[j+1]
        
        for k in range(len(nums)):
            if prefix[k] == suffix[k]:
                return k
            
        return -1

# 2nd method
class Solution:
    def pivotIndex(self, nums) -> int:
        left = 0
        total = sum(nums)
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left+=nums[i]
        return -1