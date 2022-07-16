class Solution:
    def solve(self,nums,output,index,ans,sum1):
        sum1=sum(nums)//4
        if index==len(nums):
            if len(output)==4:
                ans.append(output[:])
            return
        
        for i in range(index,len(nums)):
            if sum(nums[index:i+1])==sum1:
                output.append(nums[index:i+1])
                self.solve(nums,output,i+1,ans)
                output.pop()
            
    def makesquare(self,nums):
        ans=[]
        output=[]
        index=0
        sum1=sum(nums)//4
        self.solve(nums,output,index,ans,sum1)
        return ans
        # return True if ans else False

l=Solution()
nums=[5,5,5,5,4,4,4,4,3,3,3,3]
print(l.makesquare(nums))