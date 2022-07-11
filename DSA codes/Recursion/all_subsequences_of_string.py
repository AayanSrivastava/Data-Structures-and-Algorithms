# (output[0]=='a' or output[0]=='e' or output[0]=='i' or output[0]=='o' or output[0]=='u')
class Solution:
    def solve(self,s,output,index,ans):
        if index>=len(s):
            if output not in ans:
                ans.append(''.join(output[:]))
            return
        
        output+=(s[index])
        self.solve(s,output,index+1,ans)
        output=output[:-1]
        self.solve(s,output,index+1,ans)
    
    def subsequence(self,s):
        output=""
        ans=[]
        index=0
        self.solve(s,output,index,ans)
        return ans

l=Solution()
s="abc"
print(l.subsequence(s))