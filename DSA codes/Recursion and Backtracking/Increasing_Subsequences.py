class Solution:
    def solve(self,nums,output,index,ans):
        if index==len(nums):
            if len(output)>1 and output not in ans and all(i <= j for i, j in zip(output, output[1:])):
                ans.append(output[:])
            return
        output.append(nums[index])
        self.solve(nums,output,index+1,ans)
        
        output.pop()
        self.solve(nums,output,index+1,ans)
        
    def findSubsequences(self, nums):
        output=[]
        ans=[]
        index=0
        self.solve(nums,output,index,ans)
        return ans

l=Solution()
nums=[4,6,7,7]
print(l.findSubsequences(nums))