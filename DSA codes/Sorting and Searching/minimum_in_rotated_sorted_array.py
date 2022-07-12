def findMin(nums):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=start+(end-start)//2
        next1=(mid+1)%len(nums)
        prev=(mid+len(nums)-1)%len(nums)

        if nums[mid]<=nums[next1] and nums[mid]<=nums[prev]:
            return nums[mid]
        elif nums[mid]<=nums[end]:
            end=mid-1
        elif nums[mid]>=nums[start]:
            start=mid+1

    return 

s=[1,2,4,6,3,6]
print(findMin(s))