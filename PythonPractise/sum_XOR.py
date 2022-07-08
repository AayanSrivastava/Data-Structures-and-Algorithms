class s:
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
                
    def subsetXORSum(self, nums):
        ans=[]
        output=[]
        index=0
        self.sub1(nums,output,index,ans)
        # print(ans)
        sum=0
        for i in ans:
            s=0
            for j in i[1:]:
                s=s^j
            sum+=s
        return sum

l=s()
s=[1,3]
print(l.subsetXORSum(s))