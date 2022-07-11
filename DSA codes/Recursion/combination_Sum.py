class Solution:
    def sub1(self,nums,output,index,ans,target,sum):
        
        if index==len(nums):
            if target==sum:
                if output not in ans:
                    ans.append(output[:])
            return

        # include
        output.append(nums[index])
        sum+=nums[index]
        self.sub1(nums,output,index+1,ans,target,sum)
            
        output.pop()
        sum-=nums[index]
        self.sub1(nums,output,index+1,ans,target,sum)
            
    def combinationSum(self, candidates,target):
        output=[]
        index=0
        ans1=[]
        sum=0
        candidates.sort()
        self.sub1(candidates,output,index,ans1,target,sum)
        return ans1
l1=Solution()
s=[2,5,2,1,2]
print(l1.combinationSum(s,5))