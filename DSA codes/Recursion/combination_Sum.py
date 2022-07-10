class Solution:
    def sub1(self,nums,output,index,ans,target):
        
        if index>=len(nums):
            return
        
        if target==0:
            ans.append(output[:])
            return

            # include
        if target>=nums[index]:
            output.append(nums[index])
            self.sub1(nums,output,index+1,ans,target-nums[index])

            # exclude
            output.pop()
        self.sub1(nums,output,index+1,ans,target)
            
    def combinationSum(self, candidates,target):
        output=[]
        index=0
        ans1=[]
        self.sub1(candidates,output,index,ans1,target)
        return ans1
l1=Solution()
s=[10,1,2,7,6,1,5]
print(l1.combinationSum(s,8))