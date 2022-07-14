class Solution:
    def sub1(self,nums,output,index,ans):
        
        #base case
        if index>=len(nums):
            ans.append(''.join(output[:]))
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
        nums=list(nums)
        self.sub1(nums,output,index,ans)
        return ans
    
l=Solution()
s="AAB"
print(l.subsets(s))