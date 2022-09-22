class Solution:
    def sub(self,nums,output,index,ans,c):
        if index==len(nums):
            if len(output)==2:
                ans.append(output[:])
            return
        output.append((nums[index],index))
        self.sub(nums,output,index+1,ans,c)
        
        output.pop()
        self.sub(nums,output,index+1,ans,c)
        
    def findSubarrays(self, nums):
        output=[]
        ans=[]
        index=0
        c=[]
        self.sub(nums,output,index,ans,c)
        return ans
l=Solution()
nums=[4,2,4]
print(l.findSubarrays(nums))
