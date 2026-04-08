class Solution:
    def subarraySum(self, arr, target):
        i = 0
        window_sum = 0
        for j in range(len(arr)):
            window_sum+=arr[j]
            
            while window_sum>target:
                window_sum-=arr[i]
                i+=1
            
            if window_sum == target:
                return [i+1, j+1]
        
        return [-1]