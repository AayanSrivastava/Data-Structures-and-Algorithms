class Solution:
    def numSubarrayProductLessThanK(self, nums,  k: int) -> int:
        if k <= 1:
            return 0
        i = 0
        prod = 1
        cnt = 0
        for j in range(len(nums)):
            prod*=nums[j]

            while prod>=k:
                prod//=nums[i]
                i+=1

            cnt+=j-i+1

        return cnt