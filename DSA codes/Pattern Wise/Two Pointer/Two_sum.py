def twoSum(nums, target):
    mapper = {}
    for i, num in enumerate(nums):
        num2 = target - num

        if num2 in mapper:
            return [mapper[num2],i]
        mapper[num] = i
    return []

nums = [3,2,4]
target = 6
print(twoSum(nums, target))