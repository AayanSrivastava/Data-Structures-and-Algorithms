class Solution:
    def threeSumClosest(self, nums, target):
        min1=1001
        nums.sort()
        a=[]
        for i in range(len(nums)-2):
            l=i+1
            k=len(nums)-1
            while(l<k):
                tot=nums[i]+nums[l]+nums[k]
                a.append(abs(target-tot))
                if(abs(target-tot)<min1):
                    min1=abs(target-tot)
                    ans=tot
                if tot== target:
                    l+= 1
                    k-= 1
                elif tot<target:
                    l=l+1
                elif tot>target:
                    k=k-1
        return ans

obj=Solution()
print(obj.threeSumClosest([-1,2,1,-4],1))