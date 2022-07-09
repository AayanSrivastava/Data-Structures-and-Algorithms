class Solution:
    def threeSum(self, nums):
        a=[]
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            k=len(nums)-1
            while(l<k):
                tot=nums[i]+nums[l]+nums[k]
                if tot== 0:
                    if [nums[i], nums[l], nums[k]] not in a:
                        a.append([nums[i], nums[l], nums[k]])
                    l+= 1
                    k-= 1
                elif tot<0:
                    l=l+1
                elif tot >0:
                    k=k-1
        return a