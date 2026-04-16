class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        prefix = {0:1}
        suffix = {n-1: 1}
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]

        for j in range(n-2,-1,-1):
            suffix[j] = suffix[j+1]*nums[j+1]
        
        for k in range(n):
            ans[k] = prefix[k]*suffix[k]
        
        return ans
        
# 2nd
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]

        right = 1
        for j in range(n-1,-1,-1):
            ans[j]*=right
            right*=nums[j]
        
        return ans