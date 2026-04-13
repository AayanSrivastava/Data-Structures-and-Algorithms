class Solution:
    def waysToSplitArray(self, nums) -> int:
        prefix = {0:0}
        suffix = {len(nums)-1:nums[-1]}
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] + nums[j]
        
        cnt = 0
        for k in range(1,len(nums)):
            if prefix[k] >= suffix[k]:
                cnt+=1
            
        return cnt

# 2nd approach
class Solution:
    def waysToSplitArray(self, nums) -> int:
        left = 0
        total = sum(nums)
        cnt = 0
        for i in range(len(nums)-1):
            left+=nums[i]
            right = total - left

            if left>=right:
                cnt+=1
            
        return cnt