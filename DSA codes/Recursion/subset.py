class Solution:
    def sub1(self,nums,output,index,ans):
        
        #base case
        if index>=len(nums):
            ans.append(output[:])
            return

        # include
        output.append(nums[index])
        self.sub1(nums,output,index+1,ans)
    
        # exclude
        output.pop()
        self.sub1(nums,output,index+1,ans)
            
    def subsets(self,nums):
        output=[]
        ans=[]
        index=0
        self.sub1(nums,output,index,ans)
        return ans
    
l=Solution()
s=[1,2,3]
print(l.subsets(s))