class Solution:
    def fourSum(self, nums, target):
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                k = j+1
                l = len(nums)-1
                while k<l:
                    tot = nums[i]+nums[j]+nums[k]+nums[l]
                    if tot == target:
                        if [nums[i],nums[j],nums[k],nums[l]] not in ans:
                            ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                    elif tot > target:
                        l-=1
                    else:
                        k+=1
        return ans