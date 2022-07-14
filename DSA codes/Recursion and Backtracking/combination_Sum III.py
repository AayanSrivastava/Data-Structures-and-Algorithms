class Solution:
    def sub(self,nums,output,index,ans,k,n):
        if index==len(nums):
            if len(output)==k and sum(output)==n:
                ans.append(output[:])
            return
        
        output.append(nums[index])
        self.sub(nums,output,index+1,ans,k,n)
        output.pop()
        self.sub(nums,output,index+1,ans,k,n)

    def combinationsum(self,k,n):
        output=[]
        ans=[]
        index=0
        nums=[1,2,3,4,5,6,7,8,9]
        self.sub(nums,output,index,ans,k,n)
        return ans

l=Solution()
n=9
k=3
print(l.combinationsum(k,n))