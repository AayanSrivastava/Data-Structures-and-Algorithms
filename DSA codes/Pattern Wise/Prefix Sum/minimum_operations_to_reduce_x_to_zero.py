class Solution:
    def minOperations(self, nums , x: int) -> int:
        #can be done using sliding window
        cursum = 0
        prefixsum = {0:-1}
        max_len = -1
        total = sum(nums)-x
        if total < 0: return -1
        if total == 0: return len(nums)
        for i in range(len(nums)):
            cursum+=nums[i]

            if cursum - total in prefixsum:
                max_len = max(max_len, i - prefixsum[cursum-total])
            if cursum not in prefixsum:
                prefixsum[cursum] = i
            
        return len(nums)-max_len if max_len!=-1 else -1