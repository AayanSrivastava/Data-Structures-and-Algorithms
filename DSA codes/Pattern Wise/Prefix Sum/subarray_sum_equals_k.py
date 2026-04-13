class Solution:
    def subarraySum(self, nums, k: int) -> int:
        cursum = 0
        cnt = 0
        prefixsum = {0 : 1}
        for i in nums:
            cursum+=i
            cnt+=prefixsum.get(cursum-k,0)
            prefixsum[cursum] = prefixsum.get(cursum,0) + 1
        
        return cnt