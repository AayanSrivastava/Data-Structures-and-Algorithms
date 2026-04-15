'''make 0 -> -1 and 1 ->0, now the problem becomes maximum length subarray with sum 0'''
class Solution:
    def findMaxLength(self, nums) -> int:
        prefixsum = {0:-1}
        sum = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum+=1
            else:
                sum-=1
            if sum in prefixsum:
                max_len = max(max_len, i - prefixsum[sum])
            else:
                prefixsum[sum] = i
        return max_len