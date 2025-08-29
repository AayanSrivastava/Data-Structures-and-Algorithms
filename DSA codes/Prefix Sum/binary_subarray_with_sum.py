class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        cnt = 0
        cursum = 0
        prefixsum = {0 : 1}
        for i in nums:
            cursum+=i
            cnt+=prefixsum.get(cursum-goal, 0)
            prefixsum[cursum] = prefixsum.get(cursum, 0)+1
        return cnt