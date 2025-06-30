class Solution:
    def longestOnes(self, nums, k: int) -> int:
        maxi = 0
        for i in range(len(nums)):
            zero = 0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    zero+=1
                if zero <= k:
                    maxi = max(maxi, j-i+1)
                else:
                    break
        return maxi