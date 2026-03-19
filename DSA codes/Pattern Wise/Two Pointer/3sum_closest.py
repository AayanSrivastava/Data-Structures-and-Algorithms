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

# GFG - highest total also
class Solution:
    def closest3Sum(self, arr, target):
        arr.sort()
        mini = float('inf')
        res = float('-inf')
        for i in range(len(arr)-2):
            j,k = i+1, len(arr)-1
            while j<k:
                total = arr[i]+arr[j]+arr[k]
                diff = abs(total-target)
                if diff < mini:
                    mini = diff
                    res = total
                elif diff == mini:
                    res = max(res, total)
                    
                if total == target:
                    return res
                elif total < target:
                    j+=1
                else:
                    k-=1
        return res