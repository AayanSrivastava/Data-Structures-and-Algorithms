class Solution:
    def solve(self,s,n,output,index,ans):
        if index==len(s)   and ''.join(output[:]) not in ans:
            if len(output)==n:
                ans.append(''.join(output[:]))
            return

        output.append(s[index])
        self.solve(s,n,output,index+1,ans)
        output.pop()
        self.solve(s,n,output,index+1,ans)

    def stringg(self,s,n):
        ans=[]
        output=[]
        index=0
        s=list(s)
        self.solve(s,n,output,index,ans)
        ans.sort()
        return ans[0]

l=Solution()
n=3
s="abcdefghijklmnopqrstuvwxyz"
print(l.stringg(s,n))