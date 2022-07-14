class Solution:
    def solve(self,S,ans,index):
        if index>=len(S) and ''.join(S[:]) not in ans :
            ans.append(''.join(S[:]))
            return
        
        for i in range(index,len(S)):
            S[index],S[i]=S[i],S[index]
            self.solve(S,ans,index+1)
            # backtracking
            S[index],S[i]=S[i],S[index]
            
    def ambiguous(self, S):
        S=list(S)
        # print(S)
        ans=[]
        index=0
        self.solve(S,ans,index)
        return ans

l1=Solution()
s="123,."
print(l1.ambiguous(s))