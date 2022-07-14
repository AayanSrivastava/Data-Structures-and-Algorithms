class Solution:
    def solve(self,S,ans,index):
        if index>=len(S) and (S[:]) not in ans:
            ans.append((S[:]))
            return
        
        for i in range(index,len(S)):
            S[index],S[i]=S[i],S[index]
            self.solve(S,ans,index+1)
            # backtracking
            S[index],S[i]=S[i],S[index]
            
    def find_permutation(self, S):
        # S=list(S)
        # print(S)
        ans=[]
        index=0
        self.solve(S,ans,index)
        ans.sort()
        return ans[1]

l1=Solution()
s=[1,2,3]
print(l1.find_permutation(s))