class Solution:
    def sub2(self,nums,output,index,ans):
        if index>=len(nums):
            if output not in ans:
                ans.append(output[:])
            return

        output.append(nums[index])
        self.sub2(nums,output,index+1,ans)
        output.pop()
        self.sub2(nums,output,index+1,ans)

    def subset2(self,nums):
        output=[]
        ans=[]
        index=0
        self.sub2(nums,output,index,ans)
        return ans
l=Solution()
s=[4,1,0]
print(l.subset2(s))