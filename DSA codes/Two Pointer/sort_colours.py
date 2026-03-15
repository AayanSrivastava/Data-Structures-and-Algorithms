class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = nums.count(0)
        cnt1 = nums.count(1)
        cnt2 = nums.count(2)

        nums[:cnt0] = [0]*cnt0
        nums[cnt0:cnt0+cnt1] = [1]*cnt1
        nums[cnt0+cnt1:] = [2]*cnt2
    
# DUTCH NATIONAL FLAG
def sortColors(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # a[mid] = 0 -- swap(a[low], a[mid]), low++, mid++
        # a[mid] = 1 -- mid++
        # a[mid] = 2 -- swap(a[mid, a[high]]), h--
        
        low = mid = 0
        high = len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid] = nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high], nums[mid]
                high-=1