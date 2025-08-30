class Solution:
    def checkSubarraySum(self, nums, k) -> bool:
        cursum = 0
        prefixsum = {0 : -1}
        for i,n in enumerate(nums):
            cursum+=n
            remainder = cursum%k
            if remainder not in prefixsum:
                prefixsum[remainder] = i
            elif i - prefixsum[remainder]>1:
                return True
        return False

# 2nd 
'''
At index i, we don’t immediately add running into seen.
We add the previous remainder.
This ensures that when we see the same running again later,
the distance is at least 2 (since the current remainder was only added 
to seen after the next iteration).'''
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        running = 0
        seen = set()
        previous = 0
        for i in nums:
            running+=i
            running%=k
            if running in seen:
                return True
            seen.add(previous)
            previous = running
        return False


# Brute force
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        n = len(nums) 
        # Check all subarrays of length >= 2
        for i in range(n):
            total = nums[i]
            for j in range(i+1, n):   # subarray must be at least length 2
                total += nums[j]
                if k == 0:
                    if total == 0:   # only 0 is divisible by 0
                        return True
                else:
                    if total % k == 0:
                        return True
        return False