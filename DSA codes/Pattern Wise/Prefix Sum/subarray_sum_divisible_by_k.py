class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        cursum = 0
        cnt = 0
        prefixsum= {0 : 1}
        for i in nums:
            cursum+=i
            remainder = cursum%k
            cnt+=prefixsum.get(remainder,0)
            prefixsum[remainder] = prefixsum.get(remainder,0) + 1
        
        return cnt