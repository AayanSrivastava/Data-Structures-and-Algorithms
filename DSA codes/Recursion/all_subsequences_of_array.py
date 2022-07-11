class Solution:
    def solve(self,s,output,index,ans):
        if index>=len(s):
            ans.append(output[:])
            return
        
        output.append(s[index])
        self.solve(s,output,index+1,ans)
        output.pop()
        self.solve(s,output,index+1,ans)
    
    def subsequence(self,s):
        output=[]
        ans=[]
        index=0
        self.solve(s,output,index,ans)
        return ans

l=Solution()
s=[3,1,2]
print(l.subsequence(s))