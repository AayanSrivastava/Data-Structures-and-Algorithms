class Solution:
    def sub(self,nums,output,index,ans):
        if len(output)>4:
            return
        
        if index==len(nums) and len(output)==4:
            ans.append('.'.join(output[:]))
            return

        for i in range(index,len(nums)):
            part = nums[index:i+1]
            if (len(part)>0 and len(part)<=3) and int(part)<=255 and (index==i or part[0]!="0"):
                output.append(part)
                self.sub(nums,output,i+1,ans)
                output.pop()

    def partition(self,s):
        ans=[]
        self.sub(s,[],0,ans)
        return ans

l=Solution()
s="101023"
print(l.partition(s))