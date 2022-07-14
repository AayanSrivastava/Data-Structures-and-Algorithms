class Solution:
    def sub(self,nums,output,index,ans):
        if index==len(nums)+1:
            ans.append(output[:])
            return
        for i in range(index,len(nums)+1):
            if nums[index-1:i]==nums[index-1:i][::-1]:
                output.append(nums[index-1:i])
                self.sub(nums,output,index+1,ans)
                output.pop()

    def combinationsum(self,s):
        output=[]
        ans=[]
        index=1
        self.sub(s,output,index,ans)
        return ans

l=Solution()
s="aab"
print(l.combinationsum(s))