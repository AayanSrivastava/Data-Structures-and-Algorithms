def twoSum(nums, target):
        i = 0
        ans = []
        for j in range(i+1,len(nums)):
            two_sum = nums[i]+nums[j]
            if two_sum == target:
                ans.append(i)
                ans.append(j)
                break
            i+=1
        return ans

nums = [3,2,4]
target = 6
print(twoSum(nums, target))