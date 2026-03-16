class Solution:
    def sortedSquares(self, nums):
        i, j = 0, len(nums)-1
        ans = []
        while i<=j:
            if nums[i]**2 > nums[j]**2:
                ans.append(nums[i]**2)
                i+=1
            else:
                ans.append(nums[j]**2)
                j-=1
        return ans[::-1]

obj = Solution()
nums = [-4,-1,0,1,10]
print(obj.sortedSquares(nums))