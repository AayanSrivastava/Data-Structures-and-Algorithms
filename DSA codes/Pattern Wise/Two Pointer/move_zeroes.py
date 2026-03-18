# Wrong focus:

# "Where should zeros go?"

# Right focus:

# "Where should non-zero elements go?"

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0

        while read<len(nums):
            if nums[read]!=0:
                nums[write]=nums[read]
                write+=1
            read+=1
        
        for i in range(write, len(nums)):
            nums[i]=0
        
        return nums
obj = Solution()
nums = [0,1,3,0,12,0]
print(obj.moveZeroes(nums))