class Solution:
    def solve(self,s,index,ans):
        if index>=len(s):
            if ''.join(s[:]) not in ans and (''.join(s[:]))[::-1] not in ans:
                ans.append(''.join(s[:]))
            return
        
        for i in range(index,len(s)):
            s[index]=s[index].lower()
            s[index],s[i]=s[i],s[index]
            self.solve(s,index+1,ans)

            s[index]=s[index].upper()
            s[index],s[i]=s[i],s[index]
            self.solve(s,index+1,ans)
            # backtracking
            s[index],s[i]=s[i],s[index]
            
    def find_permutation(self, S):
        S=list(S)
        ans=[]
        index=0
        self.solve(S,index,ans)
        return ans

l1=Solution()
s="ab"
print(l1.find_permutation(s))