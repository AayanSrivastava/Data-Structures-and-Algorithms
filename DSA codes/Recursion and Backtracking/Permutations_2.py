from typing import List
class Solution:
    def solve(self,nums,ans,index):
        if index==len(nums):
            ans.append(nums[:])
            return
        
        seen = set()
        for i in range(index,len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            nums[index],nums[i]=nums[i],nums[index]
            self.solve(nums,ans,index+1)
            nums[index],nums[i]=nums[i],nums[index]
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.solve(nums,ans,0)
        return ans

obj = Solution()
nums=[1,2,3]
print(obj.permuteUnique(nums))