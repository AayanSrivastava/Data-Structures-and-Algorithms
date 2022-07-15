import math
class Solution:
    def solve(self,nums,index,ans):
        if index==len(nums):
            ans.append(nums[:])
            return
        
        for i in range(index,len(nums)):
            nums[index],nums[i]=nums[i],nums[index]
            self.solve(nums,index+1,ans)
            nums[index],nums[i]=nums[i],nums[index]

    def isperfectsquare(self,i):
        
        return 1
    def numSquarefulPerms(self, nums):
        ans=[]
        index=0
        a=[]
        b=[]
        self.solve(nums,index,ans)
        for i in ans:
            for j in range(len(i)-1):
                if (i[j]+i[j+1])**0.5 != int(math.sqrt(i[j]+i[j+1])):
                    break
            a.append(i)
                # b.append(int(math.sqrt(i[j]+i[j+1])))
            # a.append(i)
        return a
    
l=Solution()
nums=[1,17,8]
print(l.numSquarefulPerms(nums))