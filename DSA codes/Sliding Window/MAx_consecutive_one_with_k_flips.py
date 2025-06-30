def longestOnes(self, nums, k: int) -> int:
    maxi = 0
    zero = 0
    i = 0
    for j in range(len(nums)):
        if nums[j]==0:
            zero+=1
        
        while  zero > k:
            if nums[i] == 0:
                zero -=1
            i+=1

        maxi=max(maxi, j-i+1)
    return maxi