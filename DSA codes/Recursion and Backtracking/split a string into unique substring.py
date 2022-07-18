class Solution:
    def solve(self,nums,index,output,ans):
        if index==len(nums):
            output.sort()
            if len(output)==5:
                ans.append(output[:])
            return
        
        for i in range(index,len(nums)):
            if nums[index:i+1] not in output:
                output.append(nums[index:i+1])
                self.solve(nums,i+1,output,ans)
                output.pop()
            
    def split(self,nums):
        output=[]
        ans=[]
        index=0
        self.solve(nums,index,output,ans)
        return ans

l=Solution()
s="ababccc"
print(l.split(s))
