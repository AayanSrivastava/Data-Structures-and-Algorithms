def twoSum(nums, target):
    freq = {}
    ans = []
    for i, num in enumerate(nums):
        num2 = target - num

        if num2 in freq:
            return [freq[num2],i]
        freq[num]= i
    return ans

nums = [3,2,4]
target = 6
print(twoSum(nums, target))