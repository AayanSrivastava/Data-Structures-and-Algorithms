class Solution:
    def longestSubarray(self, arr, k):  
        maxi = 0
        for i in range(len(arr)):
            sum = 0
            for j in range(i,len(arr)):
                sum+=arr[j]
                if sum == k:
                    maxi = max(maxi, j-i+1)
        return maxi

# Prefix_sum
class Solution:
    def longestSubarray(self, arr, k):  
        cursum = 0
        prefixsum = {}
        maxi = 0
        for i,num in enumerate(arr):
            cursum+=num
            
            if cursum == k:
                maxi = max(maxi, i+1)
            
            if cursum-k in prefixsum:
                maxi = max(maxi, i - prefixsum[cursum-k])
                
            if cursum not in prefixsum:
                prefixsum[cursum] = i
        return maxi