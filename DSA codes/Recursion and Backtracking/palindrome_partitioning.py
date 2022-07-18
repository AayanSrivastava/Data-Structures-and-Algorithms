class Solution:
    def sub(self,nums,output,index,ans):
        if index==len(nums):
            ans.append(output[:])
            return
            
        for i in range(index,len(nums)):
            if nums[index:i+1]==nums[index:i+1][::-1]:
                output.append(nums[index:i+1])
                self.sub(nums,output,i+1,ans)
                output.pop()

    def partition(self,s):
        output=[]
        ans=[]
        index=0
        self.sub(s,output,index,ans)
        return ans

l=Solution()
s="aab"
print(l.partition(s))