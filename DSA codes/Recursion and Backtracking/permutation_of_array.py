class Solution:
    def solve(self,S,ans,index):
        if index>=len(S):
            ans.append(S[:])
            return
        
        seen= set()
        for i in range(index,len(S)):
            if S[i] in seen:
                continue
            seen.add(S[i])
            S[index],S[i]=S[i],S[index]
            self.solve(S,ans,index+1)
            # backtracking
            S[index],S[i]=S[i],S[index]
                
    def find_permutation(self, S):
        ans=[]
        index=0
        self.solve(S,ans,index)
        return sorted(ans)

l=Solution()
s=[1,2,3]
print(l.find_permutation(s))