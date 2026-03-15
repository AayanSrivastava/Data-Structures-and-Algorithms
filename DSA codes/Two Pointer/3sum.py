def threeSum(nums):
    nums.sort()
    ans = []
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        j,k = i+1, len(nums)-1
        while j<k:
            total = nums[i]+nums[j]+nums[k]
            if total == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
            elif total > 0:
                k-=1
            else:
                j+=1
    return ans
nums = [1,2,5,3,0,-1]
print(threeSum(nums))