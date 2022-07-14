class Solution:
    def sub1(self,nums,output,index,ans):
        
        #base case
        if index>=len(nums):
            ans.append(''.join(output[:]))
            return

        # include
        output.append(nums[index])
        self.sub1(nums,output,index+1,ans)
    
        # exclude
        output.pop()
        self.sub1(nums,output,index+1,ans)
            
    def subsets(self,nums):
        output=[]
        ans=[]
        index=0
        nums=list(nums)
        self.sub1(nums,output,index,ans)
        return set(ans)

    def solve(self,S,ans,index):
        if index>=len(S) and ''.join(S[:]) not in ans:
            ans.append(''.join(S[:]))
            return
        
        for i in range(index,len(S)):
            S[index],S[i]=S[i],S[index]
            self.solve(S,ans,index+1)
            # backtracking
            S[index],S[i]=S[i],S[index]
    
    def find_permutation(self, S):
        S=list(S)
        # print(S)
        ans=[]
        index=0
        a=[]
        for i in S:
            self.solve(list(i),ans,index)
        return len(ans)-1
    
l=Solution()
s="AAABBC"
print(l.find_permutation(l.subsets(s)))


# LEETCODE Letter Tiles Possibilities

# class Solution:
#     def sub1(self,nums,output,index,ans):
        
#         #base case
#         if index>=len(nums):
#             ans.append(''.join(output[:]))
#             return

#         # include
#         output.append(nums[index])
#         self.sub1(nums,output,index+1,ans)
    
#         # exclude
#         output.pop()
#         self.sub1(nums,output,index+1,ans)
            
#     def subsets(self,nums,ans1):
#         output=[]
#         index=0
#         nums=list(nums)
#         self.sub1(nums,output,index,ans1)
#         return ans1

#     def solve(self,S,ans,index):
#         if index>=len(S) and ''.join(S[:]) not in ans:
#             ans.append(''.join(S[:]))
#             return
        
#         for i in range(index,len(S)):
#             S[index],S[i]=S[i],S[index]
#             self.solve(S,ans,index+1)
#             # backtracking
#             S[index],S[i]=S[i],S[index]
    
#     def find_permutation(self, S,ans2):
#         S=list(S)
#         # print(S)
#         index=0
#         a=[]
#         for i in S:
#             self.solve(list(i),ans2,index)
#         return ans2
    
#     def numTilePossibilities(self, tiles: str) -> int:
#         ans1=[]
#         ans2=[]
#         self.subsets(tiles,ans1)
#         self.find_permutation(set(ans1),ans2)
#         return len(ans2)-1