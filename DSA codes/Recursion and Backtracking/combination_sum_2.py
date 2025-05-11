from typing import List
class Solution:
    def sub1(self,nums,output,index,ans,target):
        if target==0:
            ans.append(output[:])
            return
        if target<0 or index>=len(nums):
            return
        for i in range(index, len(nums)):
            if i > index and nums[i]==nums[i-1]:
                continue
            if nums[i]>target:
                break
            # include
            output.append(nums[i])
            self.sub1(nums,output,i+1,ans,target-nums[i])   
            output.pop()
                
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output=[]
        index=0
        ans=[]

        self.sub1(candidates,output,index,ans,target)
        return ans

obj = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(obj.combinationSum2(candidates, target))