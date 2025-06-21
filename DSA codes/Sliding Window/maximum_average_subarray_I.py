class Solution:
    def findMaxAverage(self, nums, k) -> float:
            i = 0
            window_sum=0
            maxi = float('-inf')
            for j in range(len(nums)):
                window_sum+=nums[j]

                if j - i + 1 > k:
                    window_sum-=nums[i]
                    i+=1
                
                if j-i+1 == k:
                    maxi = max(maxi, window_sum/k)
            
            return maxi