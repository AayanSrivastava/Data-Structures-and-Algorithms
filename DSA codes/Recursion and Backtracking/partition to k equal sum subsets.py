class Solution:
    def solve(self,nums,output,index,ans):
        ans1=[]
        if index==len(nums) and output not in ans1:
            ans.append(sum(output))
            ans1.append(output[:])
            return
        
        output.append(nums[index])
        self.solve(nums,output,index+1,ans)
        
        output.pop()
        self.solve(nums,output,index+1,ans)
    
    def canPartitionKSubsets(self, nums,k):
        output=[]
        index=0
        h={}
        ans=[]
        self.solve(nums,output,index,ans)
        for i in ans:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for i in h.values():
            if i==k:
                return True
            else:
                return False

l=Solution()
nums=[1,2,3,4]
k=3
print(l.canPartitionKSubsets(nums,k))