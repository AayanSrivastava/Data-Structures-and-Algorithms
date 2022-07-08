
# PERMUTATIONS OF TWO STRINGS, AND FINDING IF PERMUTATIONS OF ONE STRING CONTAIN ANY PERMUTATION OF OTHER
class Solution:
    def solve(self,S,ans,index):
        if index>=len(S):
            ans.append(''.join(S[:]))
            return
        
        for i in range(index,len(S)):
            S[index],S[i]=S[i],S[index]
            self.solve(S,ans,index+1)
            # backtracking
            S[index],S[i]=S[i],S[index]
            
    def checkInclusion(self,s1,s2):
        s1=list(s1)
        s2=list(s2)
        c=0
        ans=[]
        ans1=[]
        index=0
        index1=0
        self.solve(s1,ans,index)
        self.solve(s2,ans1,index1)
        for i in ans1:
            if i in ans:
                c+=1
        if c>=1:
            return True
        else:
            return False
l=Solution()
s1="ab"
s2="ab"
print(l.checkInclusion(s1,s2))