from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums, k) -> int:
        i = 0
        maxi = 0
        window_sum = 0
        mapper = defaultdict(int)
        for j in range(len(nums)):
            window_sum+=nums[j]
            mapper[nums[j]]+=1

            while j-i+1 > k:
                window_sum-=nums[i]
                mapper[nums[i]]-=1
                if mapper[nums[i]]==0:
                    del mapper[nums[i]]
                i+=1
            
            if j-i+1 == k and len(mapper) == k:
                maxi = max(maxi, window_sum)
        
        return maxi