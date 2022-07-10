class Solution:
    def sub1(self,nums,output,index,ans):
        
        #base case
        if index>=len(nums):
            output.append(ans)
            return

        self.sub1(nums,output,index+1,ans+nums[index])
        self.sub1(nums,output,index+1,ans)
            
    def subsets(self,nums):
        output=[]
        ans=""
        index=0
        self.sub1(nums,output,index,ans)
        return output
    
l=Solution()
s="ABC"
print(l.subsets(s))