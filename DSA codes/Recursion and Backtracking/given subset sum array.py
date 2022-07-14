class Solution:
    def sub(self,sums,output,index,ans,n,ans1):
        if index>=len(sums):
            ans1.append(output[:])
            if len(output)==n and sum(output)==0:
                ans.append(output[:])
            return
        
        output.append(sums[index])
        self.sub(sums,output,index+1,ans,n,ans1)
        
        output.pop()
        self.sub(sums,output,index+1,ans,n,ans1)
        
    def recoverArray(self,n,sums):
        output=[]
        ans=[]
        index=0
        ans1=[]
        self.sub(sums,output,index,ans,n,ans)
        # for i in ans:
        #     ans1=[]
        #     a=[]
        #     self.sub(sums,output,index,ans,n,ans1)
        return ans1
    
l=Solution()
s=[1,2,3]
n=3
print(l.recoverArray(n,s))