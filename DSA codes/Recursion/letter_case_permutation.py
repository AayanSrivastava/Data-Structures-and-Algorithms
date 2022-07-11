class Solution:
    def solve(self,s,index,ans):
        if index>=len(s):
            if ''.join(s[:]) not in ans and (''.join(s[:]))[::-1] not in ans:
                ans.append(''.join(s[:]))
            return
        op1=[]
        for i in range(index,len(s)):
            if s[i].isalpha():
                s[index]=s[index].lower()
                s[index],s[i]=s[i],s[index]
                self.solve(s,index+1,ans)

                s[index]=s[index].upper()
                s[index],s[i]=s[i],s[index]
                self.solve(s,index+1,ans)
                # backtracking
                s[index],s[i]=s[i],s[index]
            else:
                op1=ans
                op1.append(s[0])
                s.pop()
                self.solve(s,index,op1)
                
    def find_permutation(self, S):
        S=list(S)
        ans=[]
        index=0
        self.solve(S,index,ans)
        return ans

l1=Solution()
s="a1"
print(l1.find_permutation(s))