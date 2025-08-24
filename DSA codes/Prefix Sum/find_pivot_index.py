class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        pref = [0] * (n+1)
        for i in range(len(nums)):
            pref[i+1] = pref[i] + nums[i]
        
        for i in range(len(nums)):
            left_sum = pref[i]
            right_sum = pref[n] - pref[i+1]
            if left_sum - right_sum == 0:
                return i
        return -1
    

    # No prefix array
    class Solution:
        def pivotIndex(self, nums) -> int:
            total = sum(nums)
            left_sum = 0

            for i, num in enumerate(nums):
                if left_sum == total - left_sum - num:
                    return i
                left_sum += num
            return -1


#Brute force
class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)

        for i in range(n):
            left_sum = sum(nums[:i])      # sum before i
            right_sum = sum(nums[i+1:])   # sum after i
            if left_sum == right_sum:
                return i
        return -1
