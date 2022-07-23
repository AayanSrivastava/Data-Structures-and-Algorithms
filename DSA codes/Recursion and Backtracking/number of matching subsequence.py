class Solution:
    def subset(self,s,output,index,ans):
        if index==len(s) and output not in ans:
            ans.append(''.join(output[:]))
            return
        
        output.append(s[index])
        self.subset(s,output,index+1,ans)
        output.pop()
        self.subset(s,output,index+1,ans)
        
    def numMatchingSubseq(self, s,words):
        output=[]
        ans=[]
        index=0
        c=0
        s=list(s)
        self.subset(s,output,index,ans)
        for i in ans:
            if i in words:
                c+=1
        return c
    
l=Solution()
s="dsahjpjauf"
words=["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
print(l.numMatchingSubseq(s,words))