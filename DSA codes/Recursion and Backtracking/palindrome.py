# cook your dish here
class Solution:
    def solve(self,nums,index,ans):
        if index==len(nums) and (nums[:]) not in ans:
            ans.append(''.join(nums[:]))
            return
        
        for i in range(index,len(nums)):
            nums[index],nums[i]=nums[i],nums[index]
            self.solve(nums,index+1,ans)
            nums[index],nums[i]=nums[i],nums[index]

    def perm(self,s):
        ans=[]
        index=0
        s=list(s)
        self.solve(s,index,ans)
        ans.sort()
        return ans

l1=Solution()
# t=int(input())
# while t:
#     n=int(input())
#     s=input()
#     print(l1.perm(s))
#     t-=1
# n=int(input())
s="101"   
print(l1.perm(s))