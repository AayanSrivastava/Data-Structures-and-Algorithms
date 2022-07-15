class Solution:
    def solve(self,nums,index,ans,start):
        if index==len(nums) and nums[0]==start:
            ans.append(nums[:])
            return
        
        for i in range(index,len(nums)):
            nums[index],nums[i]=nums[i],nums[index]
            self.solve(nums,index+1,ans,start)
            nums[index],nums[i]=nums[i],nums[index]
            
    def circularPermutation(self,n,start):
        ans=[]
        index=0
        nums=[i for i in range(0,(2**n))]
        self.solve(nums,index,ans,start)
        return ans

l=Solution()
n=2
start=3
print(l.circularPermutation(n,start))