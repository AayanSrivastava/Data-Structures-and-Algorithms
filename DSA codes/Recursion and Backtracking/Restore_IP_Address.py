class Solution:
    def sub(self,nums,output,index,ans):
        if index==len(nums):
            if len(output)==4:
                ans.append('.'.join(output[:]))
            return

        for i in range(index,len(nums)):
            if (len(nums[index:i+1])>0 and len(nums[index:i+1])<=3) and int(nums[index:i+1])<=255 and (index==i or nums[index:i+1][0]!="0"):
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
s="101023"
print(l.partition(s))