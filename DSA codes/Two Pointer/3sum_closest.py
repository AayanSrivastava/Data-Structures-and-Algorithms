def threeSumClosest(self, nums, target):
    nums.sort()
    mini = float('inf')
    res = 0
    for i in range(len(nums)-2):
        j,k = i+1, len(nums)-1
        while j<k:
            total = nums[i]+nums[j]+nums[k]
            diff = abs(total-target)
            if diff < mini:
                mini = diff
                res = total

            if total == target:
                return res
            elif total < target:
                j+=1
            else:
                k-=1
    return res